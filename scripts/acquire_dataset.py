from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tarfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
USER_AGENT = "evrp-benchmark-datasets-acquisition/1.0 (research reproducibility)"
DATA_EXTENSIONS = {".evrp", ".txt", ".csv", ".xlsx", ".xls", ".json", ".dat", ".vrp", ".xml", ".tsv", ".geojson"}
MAX_DOWNLOAD_BYTES = 2 * 1024 * 1024 * 1024


class AcquisitionError(RuntimeError):
    pass


def request(url: str, *, headers=None, timeout=60, max_bytes=MAX_DOWNLOAD_BYTES) -> bytes:
    hdrs = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = response.read(max_bytes + 1)
            if len(data) > max_bytes:
                raise AcquisitionError(f"Response exceeds configured {max_bytes} byte limit: {url}")
            return data
    except urllib.error.HTTPError as exc:
        raise AcquisitionError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise AcquisitionError(f"Network error for {url}: {exc}") from exc


def get_json(url: str, headers=None):
    raw = request(url, headers={"Accept": "application/json", **(headers or {})})
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise AcquisitionError(f"Expected JSON from {url}: {exc}") from exc


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._") or "download"


def save_url(url: str, target: Path, *, headers=None):
    target.parent.mkdir(parents=True, exist_ok=True)
    hdrs = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    digest = hashlib.sha256()
    total = 0
    try:
        with urllib.request.urlopen(req, timeout=120) as response, target.open("wb") as dst:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_DOWNLOAD_BYTES:
                    raise AcquisitionError(f"Download exceeds configured {MAX_DOWNLOAD_BYTES} byte limit: {url}")
                digest.update(chunk)
                dst.write(chunk)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    if total == 0:
        raise AcquisitionError(f"Downloaded an empty file: {url}")
    return {"url": url, "path": str(target), "bytes": total, "sha256": digest.hexdigest()}


def safe_extract_zip(archive: Path, destination: Path):
    destination.mkdir(parents=True, exist_ok=True)
    extracted = []
    with zipfile.ZipFile(archive) as zf:
        total_uncompressed = sum(i.file_size for i in zf.infolist() if not i.is_dir())
        if total_uncompressed > MAX_DOWNLOAD_BYTES:
            raise AcquisitionError(f"ZIP expands beyond configured {MAX_DOWNLOAD_BYTES} byte limit: {archive.name}")
        bad = zf.testzip()
        if bad:
            raise AcquisitionError(f"Corrupt ZIP member: {bad}")
        for info in zf.infolist():
            name = info.filename.replace("\\", "/")
            rel = PurePosixPath(name)
            if rel.is_absolute() or ".." in rel.parts or (rel.parts and ":" in rel.parts[0]):
                raise AcquisitionError(f"Unsafe ZIP member path: {name}")
            if info.is_dir():
                continue
            out = destination.joinpath(*rel.parts)
            out.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as src, out.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            extracted.append(out)
    return extracted


def safe_extract_tar(archive: Path, destination: Path):
    destination.mkdir(parents=True, exist_ok=True)
    extracted = []
    with tarfile.open(archive, "r:*") as tf:
        members = tf.getmembers()
        total_uncompressed = sum(m.size for m in members if m.isfile())
        if total_uncompressed > MAX_DOWNLOAD_BYTES:
            raise AcquisitionError(f"TAR expands beyond configured {MAX_DOWNLOAD_BYTES} byte limit: {archive.name}")
        for member in members:
            rel = PurePosixPath(member.name.replace("\\", "/"))
            if rel.is_absolute() or ".." in rel.parts or member.issym() or member.islnk():
                raise AcquisitionError(f"Unsafe TAR member: {member.name}")
            if not member.isfile():
                continue
            src = tf.extractfile(member)
            if src is None:
                continue
            out = destination.joinpath(*rel.parts)
            out.parent.mkdir(parents=True, exist_ok=True)
            with src, out.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            extracted.append(out)
    return extracted


def extract_archives(directory: Path):
    """Extract nested ZIP/TAR files safely; keep original archives as provenance."""
    for _ in range(3):
        archives = [p for p in directory.rglob("*") if p.is_file() and (
            p.suffix.lower() == ".zip" or p.name.lower().endswith((".tar.gz", ".tgz", ".tar"))
        )]
        if not archives:
            break
        for archive in archives:
            marker = archive.with_name(archive.name + ".extracted")
            if marker.exists():
                continue
            target = archive.parent / (archive.stem.replace(".tar", "") + "_contents")
            if archive.suffix.lower() == ".zip":
                safe_extract_zip(archive, target)
            else:
                safe_extract_tar(archive, target)
            marker.write_text("extracted\n", encoding="utf-8")


class AnchorParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._href = None
        self._text = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._href is not None:
            self.links.append((self._href, " ".join(" ".join(self._text).split())))
            self._href = None
            self._text = []


def download_vrp_rep(cfg, stage):
    page = cfg["source_url"]
    html = request(page).decode("utf-8", "replace")
    parser = AnchorParser()
    parser.feed(html)
    candidates = []
    for href, label in parser.links:
        text = label.lower()
        if any(word in text for word in ("download dataset", "dataset download", "download instances")):
            candidates.append(urllib.parse.urljoin(page, href))
    if not candidates:
        # VRP-REP sometimes uses a direct download link whose visible label is terse.
        candidates = [urllib.parse.urljoin(page, href) for href, label in parser.links
                      if re.search(r"(download|file|dataset).*(zip|dat|txt)|\.(zip|tar|gz)(\?|$)", href, re.I)]
    if not candidates:
        raise AcquisitionError("VRP-REP page was reachable but no official dataset download link could be identified.")
    downloaded = []
    for i, url in enumerate(dict.fromkeys(candidates)):
        name = safe_name(urllib.parse.urlparse(url).path.split("/")[-1] or f"dataset-{i+1}.zip")
        if "." not in name:
            name += ".zip"
        downloaded.append(save_url(url, stage / "downloads" / name))
    return downloaded, {"source_page": page, "adapter": "vrp_rep_html_link_discovery"}


def download_mendeley(cfg, stage):
    dataset_id, version = cfg["source_id"], str(cfg["version"])
    base = f"https://api.data.mendeley.com/datasets/{dataset_id}"
    headers = {"Accept": "application/vnd.mendeley-public-dataset.1+json"}
    token = os.getenv("MENDELEY_ACCESS_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    # Dataset and files endpoints are documented by Digital Commons Data.
    metadata = get_json(f"{base}?version={urllib.parse.quote(version)}", headers=headers)
    files_url = f"https://api.data.mendeley.com/datasets/publics/{dataset_id}/files?version={urllib.parse.quote(version)}&$limit=500"
    files = get_json(files_url, headers=headers)
    if isinstance(files, dict):
        files = files.get("results") or files.get("files") or []
    if not isinstance(files, list) or not files:
        raise AcquisitionError("Mendeley API returned no public file listing.")
    downloads = []
    for item in files:
        file_id = item.get("id") or item.get("file_id")
        filename = item.get("filename") or item.get("name") or (str(file_id) if file_id else None)
        if not file_id or not filename:
            continue
        details = item
        if not (details.get("content_details") or {}).get("download_url"):
            details = get_json(f"https://api.data.mendeley.com/datasets/publics/{dataset_id}/files/{file_id}?version={version}", headers=headers)
        content = details.get("content_details") or {}
        url = content.get("download_url") or details.get("download_url")
        if not url:
            # Documented redirect endpoint for a public file.
            url = f"https://api.data.mendeley.com/datasets/{dataset_id}/files/{file_id}/file_downloaded?version={version}"
        target = stage / "downloads" / safe_name(filename)
        downloads.append(save_url(url, target, headers=headers))
    if not downloads:
        # Public dataset zip endpoint fallback; the API returns a download URL or redirect.
        zip_meta_url = f"https://api.data.mendeley.com/datasets/{dataset_id}/zip?version={version}"
        zip_meta = get_json(zip_meta_url, headers=headers)
        zip_url = zip_meta.get("url")
        if not zip_url:
            raise AcquisitionError("Mendeley dataset file metadata did not provide downloadable files or a ZIP URL.")
        downloads.append(save_url(zip_url, stage / "downloads" / f"{dataset_id}-v{version}.zip", headers=headers))
    licence = metadata.get("licence") or metadata.get("license") or metadata.get("licence_id")
    if isinstance(licence, dict):
        licence_id = licence.get("id")
        licence = licence.get("spdx_id") or licence.get("name") or licence.get("title") or licence_id
        if licence_id and (not licence or str(licence) == str(licence_id)):
            try:
                licence_record = get_json(
                    f"https://api.data.mendeley.com/active-data-entities/licences/{urllib.parse.quote(str(licence_id), safe='')}",
                    headers=headers,
                )
                licence = (licence_record.get("name") or licence_record.get("title") or
                           licence_record.get("spdx_id") or licence_id)
            except AcquisitionError:
                licence = licence_id
    elif isinstance(licence, str) and re.fullmatch(r"[0-9a-fA-F-]{36}", licence):
        try:
            licence_record = get_json(
                f"https://api.data.mendeley.com/active-data-entities/licences/{urllib.parse.quote(licence, safe='')}",
                headers=headers,
            )
            licence = licence_record.get("name") or licence_record.get("title") or licence_record.get("spdx_id") or licence
        except AcquisitionError:
            pass
    return downloads, {"source_page": cfg["version_url"], "adapter": "mendeley_public_api",
                       "api_license_metadata": licence, "api_version": metadata.get("version")}


def download_zenodo(cfg, stage):
    record_id = cfg["source_id"]
    metadata = get_json(f"https://zenodo.org/api/records/{record_id}")
    files = metadata.get("files", [])
    if not files:
        raise AcquisitionError("Zenodo API record contains no files.")
    # Prefer canonical data archives; include structured manifests and small tabular descriptors.
    names = [str(f.get("key", "")) for f in files]
    archives = [f for f in files if str(f.get("key", "")).lower().endswith((".zip", ".tar", ".tar.gz", ".tgz"))]
    selected = []
    if archives:
        selected.extend(archives)
    else:
        selected.extend(files)
    for f in files:
        key = str(f.get("key", "")).lower()
        if key.endswith((".csv", ".json", ".tex", ".md", ".txt")) and f not in selected:
            selected.append(f)
    downloads = []
    for f in selected:
        key = f.get("key")
        links = f.get("links") or {}
        url = links.get("content") or links.get("download") or f"https://zenodo.org/api/records/{record_id}/files/{urllib.parse.quote(key)}/content"
        downloads.append(save_url(url, stage / "downloads" / safe_name(key)))
    lic = (metadata.get("metadata") or {}).get("license")
    if isinstance(lic, dict):
        lic = lic.get("id") or lic.get("title")
    return downloads, {"source_page": cfg["version_url"], "adapter": "zenodo_records_api",
                       "api_license_metadata": lic, "record_version": metadata.get("metadata", {}).get("version"),
                       "record_doi": metadata.get("doi"), "record_files": names}


def download_dryad(cfg, stage):
    doi = cfg["source_id"]
    encoded = urllib.parse.quote(f"doi:{doi}", safe="")
    metadata = get_json(f"https://datadryad.org/api/v2/datasets/{encoded}")
    version = metadata.get("latestVersion") or metadata.get("version") or {}
    version_id = version.get("id") or metadata.get("latestVersionId")
    if not version_id:
        versions = get_json(f"https://datadryad.org/api/v2/datasets/{encoded}/versions")
        if isinstance(versions, list) and versions:
            version_id = versions[-1].get("id")
    if not version_id:
        raise AcquisitionError("Dryad API did not expose a published version ID.")
    files = get_json(f"https://datadryad.org/api/v2/versions/{version_id}/files")
    if isinstance(files, dict):
        files = files.get("_embedded", {}).get("stash:files", files.get("files", []))
    if not isinstance(files, list) or not files:
        raise AcquisitionError("Dryad API returned no files for the selected version.")
    downloads = []
    for item in files:
        file_id = item.get("id")
        filename = item.get("path") or item.get("filename") or f"dryad-file-{file_id}"
        link_map = item.get("_links") or {}
        download_link = link_map.get("download") or {}
        url = item.get("downloadUrl") or item.get("download_url") or download_link.get("href") or (
            f"https://datadryad.org/api/v2/files/{file_id}/download" if file_id else None)
        if url:
            downloads.append(save_url(url, stage / "downloads" / safe_name(Path(filename).name)))
    if not downloads:
        raise AcquisitionError("Dryad API file records did not contain downloadable file URLs.")
    licence = metadata.get("license") or metadata.get("licenseName") or version.get("license")
    return downloads, {"source_page": cfg["version_url"], "adapter": "dryad_api_v2",
                       "api_license_metadata": licence, "dryad_version_id": version_id}


def download_github(cfg, stage):
    owner_repo = cfg["source_id"]
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    metadata = get_json(f"https://api.github.com/repos/{owner_repo}", headers=headers)
    branch = metadata.get("default_branch", "main")
    commit = get_json(f"https://api.github.com/repos/{owner_repo}/commits/{urllib.parse.quote(branch, safe='')}", headers=headers)
    sha = commit.get("sha")
    if not sha:
        raise AcquisitionError("GitHub API did not return a branch commit SHA.")
    licence = (metadata.get("license") or {}).get("spdx_id")
    url = f"https://api.github.com/repos/{owner_repo}/tarball/{sha}"
    downloaded = [save_url(url, stage / "downloads" / f"{owner_repo.split('/')[-1]}-{sha[:12]}.tar.gz", headers=headers)]
    return downloaded, {"source_page": cfg["version_url"], "adapter": "github_api_tarball",
                        "api_license_metadata": licence, "resolved_commit": sha, "default_branch": branch}


def download_dimacs_derived(cfg, stage):
    # DIMACS defines the 240 capacity variants as two charger-capacity settings
    # derived from the 120 Montoya base instances. Acquire the official base set;
    # never fabricate 240 independent source files or infer the licence.
    base_cfg = {"source_url": "https://www.vrp-rep.org/datasets/item/2016-0020.html"}
    downloaded, metadata = download_vrp_rep(base_cfg, stage)
    metadata.update({"adapter": "dimacs_spec_plus_vrp_rep_base",
                     "derived_from": "EVRP-003",
                     "derived_variants": [1, 2],
                     "note": "DIMACS defines two charger-capacity variants per Montoya base instance. A domain-specific transformation and source-rights review are still required."})
    return downloaded, metadata


ADAPTERS = {
    "vrp_rep": download_vrp_rep,
    "mendeley": download_mendeley,
    "zenodo": download_zenodo,
    "dryad": download_dryad,
    "github": download_github,
    "dimacs_derived": download_dimacs_derived,
}


def validate_inventory(directory: Path, cfg):
    files = [p for p in directory.rglob("*") if p.is_file() and not p.name.endswith(".extracted")]
    data_files = [p for p in files if p.suffix.lower() in DATA_EXTENSIONS]
    problems = []
    if not data_files:
        problems.append("No recognized dataset files found after extraction.")
    for p in data_files:
        if p.stat().st_size == 0:
            problems.append(f"Empty data file: {p.relative_to(directory)}")
        if p.suffix.lower() == ".zip":
            try:
                with zipfile.ZipFile(p) as zf:
                    bad = zf.testzip()
                    if bad:
                        problems.append(f"Corrupt nested ZIP member {bad} in {p.name}")
            except Exception as exc:
                problems.append(f"Invalid ZIP {p.name}: {exc}")
        elif p.suffix.lower() == ".xlsx":
            try:
                with zipfile.ZipFile(p) as zf:
                    if "[Content_Types].xml" not in zf.namelist() or "xl/workbook.xml" not in zf.namelist():
                        problems.append(f"Invalid XLSX workbook structure: {p.name}")
                    bad = zf.testzip()
                    if bad:
                        problems.append(f"Corrupt XLSX member {bad} in {p.name}")
            except Exception as exc:
                problems.append(f"Invalid XLSX {p.name}: {exc}")
        elif p.suffix.lower() == ".json":
            try:
                json.loads(p.read_text(encoding="utf-8"))
            except Exception as exc:
                problems.append(f"Invalid JSON {p.name}: {exc}")
        elif p.suffix.lower() == ".csv":
            try:
                import csv
                with p.open(encoding="utf-8-sig", newline="") as stream:
                    rows = csv.reader(stream)
                    header = next(rows, None)
                    first_record = next(rows, None)
                    if not header or not first_record:
                        problems.append(f"CSV must contain a header and at least one data row: {p.name}")
            except Exception as exc:
                problems.append(f"Invalid CSV {p.name}: {exc}")
    method = cfg.get("count_method", "unknown")
    count = None
    if method == "instance_files":
        candidates = [p for p in data_files if p.suffix.lower() in {".evrp", ".txt", ".dat", ".vrp"} and
                      p.name.lower() not in {"readme.txt", "description.txt"}]
        if cfg["dataset_id"] == "EVRP-011":
            candidates = [p for p in data_files if p.suffix.lower() == ".csv" and re.match(r"^[rc]\d+_c\d+b\d+", p.stem, re.I)]
        count = len(candidates)
        if count == 0:
            problems.append("No instance files matched the dataset-specific instance filename rule.")
    # XLSX/CSV/JSON collections require semantic/domain parsers before publishing counts.
    inventory = []
    for p in sorted(data_files):
        inventory.append({"path": p.relative_to(directory).as_posix(), "bytes": p.stat().st_size,
                          "sha256": sha256(p), "extension": p.suffix.lower()})
    return {"status": "passed" if not problems else "failed", "errors": problems,
            "files_total": len(files), "recognized_data_files": len(data_files),
            "instance_count": count, "count_method": method, "inventory": inventory}


def load_source(did):
    config = json.loads((ROOT / "acquisition" / "sources.json").read_text(encoding="utf-8"))
    try:
        return config["sources"][did]
    except KeyError:
        raise AcquisitionError(f"Dataset {did} is not an acquisition target.")


def write_output(name, value):
    path = os.getenv("GITHUB_OUTPUT")
    if path:
        with open(path, "a", encoding="utf-8") as stream:
            stream.write(f"{name}={str(value).lower() if isinstance(value, bool) else value}\n")



def update_repository_counts(cfg, result):
    """Update integration metadata only after a successful, licence-cleared acquisition."""
    if not result.get("commit_allowed") or result.get("validation", {}).get("status") != "passed":
        return
    registry_path = ROOT / "data/registry/evrp_dataset_registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    dataset = next(d for d in registry["datasets"] if d["dataset_id"] == cfg["dataset_id"])
    dataset["local_status"] = "acquired_and_schema_validated"
    dataset["acquired_file_count"] = result["validation"]["recognized_data_files"]
    dataset["acquired_instance_count"] = result["validation"].get("instance_count")
    dataset["acquisition_validation"] = {
        "status": "passed",
        "level": "archive_integrity_and_file_schema",
        "validated_utc": result.get("completed_utc"),
        "version": result.get("version"),
        "license_gate": result.get("license_gate"),
        "source_url": result.get("source_url"),
        "resolved_commit": (result.get("adapter_metadata") or {}).get("resolved_commit"),
        "checksums": [{"path": x["path"], "sha256": x["sha256"], "bytes": x["bytes"]}
                      for x in result["validation"]["inventory"]],
    }
    # Parser-level count remains separate and is not inflated by generic file checks.
    dataset.setdefault("local_instance_count", 0)
    registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    card_path = ROOT / cfg["destination"] / "dataset.json"
    if card_path.exists():
        card = json.loads(card_path.read_text(encoding="utf-8"))
        card["local_status"] = dataset["local_status"]
        card["acquired_file_count"] = dataset["acquired_file_count"]
        card["acquired_instance_count"] = dataset["acquired_instance_count"]
        card["acquisition_validation"] = dataset["acquisition_validation"]
        card_path.write_text(json.dumps(card, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Append an immutable acquisition snapshot and checksums to the repository manifest.
    manifest_path = ROOT / "data/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {
        "manifest_version": "1.1", "source_snapshots": [], "files": []
    }
    snapshot_id = f"ACQ-{cfg['dataset_id']}-{safe_name(str(cfg['version']))}"
    manifest["source_snapshots"] = [x for x in manifest.get("source_snapshots", [])
                                    if x.get("snapshot_id") != snapshot_id]
    manifest["files"] = [x for x in manifest.get("files", [])
                         if not x.get("path", "").startswith(cfg["destination"] + "/")]
    committed_files = []
    destination = ROOT / cfg["destination"]
    for path in sorted(destination.rglob("*")):
        if (path.is_file() and path.suffix.lower() in DATA_EXTENSIONS
                and path.name.lower() not in {"readme.md", "dataset.json"}
                and "_source_archives" not in path.parts):
            committed_files.append({
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            })
    manifest.setdefault("source_snapshots", []).append({
        "id": snapshot_id,
        "snapshot_id": snapshot_id,
        "dataset_id": cfg["dataset_id"],
        "source_url": cfg["source_url"],
        "version": cfg["version"],
        "license": cfg.get("license_spdx"),
        "license_evidence_url": cfg.get("license_evidence_url"),
        "snapshot_status": "acquired_and_schema_validated",
        "files": len(committed_files),
        "acquired_instance_count": result["validation"].get("instance_count"),
        "resolved_commit": (result.get("adapter_metadata") or {}).get("resolved_commit"),
    })
    manifest.setdefault("files", []).extend(committed_files)
    manifest["manifest_version"] = "1.1"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    # Refresh the status CSV without changing parser-validated counts.
    csv_path = ROOT / "data/acquisition_status.csv"
    import csv
    rows = []
    with csv_path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    for row in rows:
        if row["dataset_id"] == cfg["dataset_id"]:
            row["local_status"] = dataset["local_status"]
            row["acquired_file_count"] = str(dataset["acquired_file_count"])
            row["acquired_instance_count"] = "" if dataset["acquired_instance_count"] is None else str(dataset["acquired_instance_count"])
            row["next_action"] = "add domain parser and run parser-level validation"
    for field in ("acquired_file_count", "acquired_instance_count"):
        if field not in fieldnames:
            fieldnames.append(field)
    with csv_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    # Update README integration badge/count only after acquisition validation succeeds.
    integrated = sum(d.get("local_status") in {"locally_ingested_and_parser_validated", "acquired_and_schema_validated"}
                     for d in registry["datasets"])
    parser_instances = sum(d.get("local_instance_count", 0) for d in registry["datasets"]
                           if d.get("local_status") == "locally_ingested_and_parser_validated")
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    readme = re.sub(r"(locally%20integrated-)[0-9]+", rf"\g<1>{integrated}", readme)
    readme = re.sub(r"(instances%20validated-)[0-9]+", rf"\g<1>{parser_instances}", readme)
    readme = re.sub(r"\| Locally integrated datasets \| \*\*[0-9]+\*\* \|",
                    f"| Locally integrated datasets | **{integrated}** |", readme)
    readme = re.sub(r"\| Parser-validated instances \| \*\*[0-9]+\*\* \|",
                    f"| Parser-validated instances | **{parser_instances}** |", readme)
    remaining = len(registry["datasets"]) - integrated
    readme = re.sub(
        r"\| Additional source folders \| \*\*[0-9]+\*\* \|",
        f"| Additional source folders | **{remaining}** |", readme)
    status_text = (
        f"**Corpus status (2 November 2026):** {len(registry['datasets'])} curated source collections are catalogued. "
        f"{integrated} collections currently have raw files locally integrated; {parser_instances} instances have passed "
        f"the implemented semantic parsers. The remaining {remaining} source folders are catalogued but do not yet contain "
        f"licence-cleared, validated raw data."
    )
    readme = re.sub(r"> \*\*Corpus status \(2 November 2026\):\*\*.*?(?=\n\n## At a glance)",
                    "> " + status_text, readme, flags=re.S)
    readme_path.write_text(readme, encoding="utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--staging", default="acquisition-staging")
    args = parser.parse_args()
    cfg = load_source(args.dataset)
    stage = Path(args.staging) / args.dataset
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True, exist_ok=True)
    result = {"dataset_id": args.dataset, "dataset_name": cfg["name"], "source_url": cfg["source_url"],
              "version": cfg["version"], "started_utc": datetime.now(timezone.utc).isoformat(),
              "license_gate": cfg["license_gate"], "redistribution_allowed": cfg["redistribute"],
              "license_evidence": cfg["license_evidence"], "license_evidence_url": cfg.get("license_evidence_url"),
              "downloads": [], "validation": None}
    try:
        downloaded, adapter_meta = ADAPTERS[cfg["adapter"]](cfg, stage)
        result["downloads"] = downloaded
        result["adapter_metadata"] = adapter_meta
        extract_archives(stage / "downloads")
        inventory = validate_inventory(stage / "downloads", cfg)
        result["validation"] = inventory
        # A legal gate requires both explicit configuration evidence and no contradictory source metadata.
        actual_license = str(adapter_meta.get("api_license_metadata") or "").strip().lower().replace("_", "-")
        expected = str(cfg.get("license_spdx") or "").lower()
        if expected and actual_license:
            normalized = actual_license.replace(" ", "")
            expected_norm = expected.lower().replace("-", "").replace(" ", "")
            actual_norm = normalized.replace("-", "").replace(" ", "")
            if expected_norm not in actual_norm and actual_norm not in expected_norm:
                result["license_gate"] = "manual_review"
                result["redistribution_allowed"] = False
                result["license_evidence"] += f" API licence metadata did not match expected {expected}: {adapter_meta.get('api_license_metadata')!r}."
        result["completed_utc"] = datetime.now(timezone.utc).isoformat()
        result["outcome"] = "validated" if inventory["status"] == "passed" else "validation_failed"
        if inventory["status"] != "passed":
            raise AcquisitionError("; ".join(inventory["errors"]))
        # Only CC BY/CC0 datasets with explicit verified terms are eligible for a PR.
        commit_allowed = bool(result["redistribution_allowed"] and result["license_gate"] == "verified")
        result["commit_allowed"] = commit_allowed
        if commit_allowed:
            destination = ROOT / cfg["destination"]
            destination.mkdir(parents=True, exist_ok=True)
            # Preserve source README/dataset card already in the repo; copy only downloaded/extracted data.
            for item in (stage / "downloads").iterdir():
                if item.is_dir():
                    target = destination / item.name
                    shutil.copytree(item, target, dirs_exist_ok=True)
                elif item.is_file() and not item.name.endswith(".extracted"):
                    # Keep the source archive as provenance alongside extracted files.
                    if item.suffix.lower() in {".zip", ".gz", ".tgz", ".tar"}:
                        shutil.copy2(item, destination / "_source_archives" / item.name)
                    elif item.suffix.lower() in DATA_EXTENSIONS:
                        target = destination / item.name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(item, target)
            result["repository_destination"] = cfg["destination"]
            update_repository_counts(cfg, result)
        else:
            result["repository_destination"] = None
            result["manual_review_required"] = True
        write_output("outcome", result["outcome"])
        write_output("commit_allowed", commit_allowed)
        write_output("dataset_id", args.dataset)
        write_output("dataset_name", cfg["name"])
        write_output("repository_destination", result.get("repository_destination") or "")
        write_output("file_count", inventory["recognized_data_files"])
        write_output("instance_count", inventory.get("instance_count") if inventory.get("instance_count") is not None else "unknown")
        write_output("license_gate", result["license_gate"])
    except Exception as exc:
        result["outcome"] = "acquisition_failed"
        result["error"] = f"{type(exc).__name__}: {exc}"
        write_output("outcome", "acquisition_failed")
        write_output("commit_allowed", False)
        write_output("dataset_id", args.dataset)
        write_output("dataset_name", cfg["name"])
        write_output("license_gate", result.get("license_gate", "manual_review"))
        (stage / "acquisition_report.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        raise
    finally:
        report = stage / "acquisition_report.json"
        report.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
