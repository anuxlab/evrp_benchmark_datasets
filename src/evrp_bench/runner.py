from pathlib import Path
import argparse, json, csv, sys
from .parsers import parse_evrp, parse_solomon_evrptw, validate_record
from .compatibility import assess
from .registry import load_registry

def inspect_file(path: Path):
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:4000].upper()
        if "NODE_COORD_SECTION" in head or "TYPE: EVRP" in head or "TYPE: EVRP" in path.read_text(encoding="utf-8", errors="replace")[:1000].upper():
            rec = parse_evrp(path)
        else:
            rec = parse_solomon_evrptw(path)
        errors = validate_record(rec)
        rec["validation"] = {"status":"passed" if not errors else "failed", "errors":errors}
        rec["compatibility"] = assess(rec)
        return rec
    except Exception as e:
        return {"name":path.name, "format":"unknown", "validation":{"status":"failed","errors":[f"parser exception: {type(e).__name__}: {e}"]},"compatibility":[]}

def attach_provenance(record, path: Path, root: Path, registry: dict):
    """Attach a stable dataset/publication citation chain to every local instance."""
    rel = path.relative_to(root).as_posix()
    mapping = {
        "mavrovouniotis-upload/": ("EVRP-001", "LOCAL-001"),
        "mendeley-evrptw/": ("EVRP-002", "LOCAL-002"),
    }
    match = next(((did, sid) for prefix, (did, sid) in mapping.items() if prefix in rel), None)
    if match:
        did, sid = match
        ds = next(x for x in registry["datasets"] if x["dataset_id"] == did)
        record["provenance"] = {
            "dataset_id": did,
            "snapshot_id": sid,
            "dataset_name": ds["name"],
            "dataset_doi": ds.get("dataset_doi"),
            "dataset_source_url": ds["official_source_url"],
            "citation_ids": ds["related_citation_ids"],
            "citation_dois": [registry["citation_sources"][cid].get("doi") for cid in ds["related_citation_ids"]],
            "local_source_path": rel,
        }
    else:
        record["provenance"] = {"dataset_id": None, "status": "unmapped_local_file", "local_source_path": rel}
    return record


def select_input_paths(root: Path, sample: bool = False):
    all_paths=sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".evrp",".txt"} and p.name.lower() not in {"readme.txt","readme.md"})
    if not sample:
        return all_paths
    selected=[]
    for suffix in (".evrp", ".txt"):
        group=[p for p in all_paths if p.suffix.lower()==suffix]
        if group:
            selected.extend([group[0]] if len(group)==1 else [group[0], group[-1]])
    return selected


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--data", default="data/raw")
    ap.add_argument("--out", default="reports")
    ap.add_argument("--sample", action="store_true", help="Inspect up to two representative files per supported format")
    args=ap.parse_args()
    root=Path(args.data); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    all_paths=select_input_paths(root, sample=False)
    paths=select_input_paths(root, sample=args.sample)
    registry_path = Path("data/registry/evrp_dataset_registry.json")
    registry = load_registry(registry_path) if registry_path.exists() else {"datasets": [], "citation_sources": {}}
    records=[attach_provenance(inspect_file(p), p, root, registry) for p in paths]
    summary={"files_discovered":len(records), "files_available":len(all_paths), "sample_mode":bool(args.sample),
             "passed":sum(x["validation"]["status"]=="passed" for x in records),
             "failed":sum(x["validation"]["status"]=="failed" for x in records),
             "formats":{}}
    for x in records: summary["formats"][x["format"]]=summary["formats"].get(x["format"],0)+1
    (out/"dataset_report.json").write_text(json.dumps({"summary":summary,"instances":records},indent=2))
    fields=["name","format","dataset_id","dataset_doi","citation_ids","citation_dois","customer_count","station_count","depot_count","vehicles","capacity","energy_capacity","battery_capacity_Q","vehicle_capacity_C","validation_status"]
    with (out/"dataset_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore"); w.writeheader()
        for x in records:
            w.writerow({**x, "dataset_id": x.get("provenance",{}).get("dataset_id"), "dataset_doi": x.get("provenance",{}).get("dataset_doi"), "citation_ids": ";".join(x.get("provenance",{}).get("citation_ids",[])), "citation_dois": ";".join(str(z) for z in x.get("provenance",{}).get("citation_dois",[]) if z), "validation_status":x["validation"]["status"]})
    md=["# Dataset inspection report","",f"- Discovered: **{summary['files_discovered']}**",f"- Passed: **{summary['passed']}**",f"- Failed: **{summary['failed']}**","", "## Formats"]
    md += [f"- `{k}`: {v}" for k,v in sorted(summary["formats"].items())]
    md += ["","## Per-instance validation","", "| Instance | Dataset | Dataset DOI | Paper/data DOI(s) | Format | Validation |","|---|---|---|---|---|---|"]
    for x in records:
        md.append(f"| {x['name']} | {x.get('provenance',{}).get('dataset_id','unmapped')} | {x.get('provenance',{}).get('dataset_doi') or '—'} | {', '.join(str(z) for z in x.get('provenance',{}).get('citation_dois',[]) if z) or '—'} | {x['format']} | {x['validation']['status']} |")
    md += ["","## Compatibility","", "Compatibility labels are data-capability assessments, not route feasibility or solver certificates.", ""]
    for x in records:
        md += [f"### {x['name']}"]
        md += [f"- **{c['problem']} — {c['status']}**: {c['reason']}" for c in x["compatibility"]]
    (out/"dataset_report.md").write_text("\\n".join(md))
    (out/"source_registry_snapshot.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False))
    print(json.dumps(summary,indent=2))
    if summary["failed"]: sys.exit(1)
if __name__=="__main__": main()
