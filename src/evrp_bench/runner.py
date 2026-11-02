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



DATASET_FOLDER_MAP = {
    "EVRP-001": "mavrovouniotis-upload",
    "EVRP-002": "mendeley-evrptw",
    "EVRP-003": "montoya-nonlinear-charging",
    "EVRP-004": "froger-capacitated-stations",
    "EVRP-005": "goeke-schneider-mixed-fleet",
    "EVRP-006": "felipe-multiple-technologies",
    "EVRP-007": "akbay-two-echelon",
    "EVRP-008": "v2g-dynamic-pricing",
    "EVRP-009": "gradient-aware-evrptw",
    "EVRP-010": "charging-station-energy-differences",
    "EVRP-011": "evrp-backhauls-uncertainty",
    "EVRP-012": "low-emission-zones-mixed-fleet",
    "EVRP-013": "electric-dial-a-ride",
    "EVRP-014": "electric-vehicle-drone-routing",
    "EVRP-015": "electric-shuttle-darp",
}

VARIANT_ALIASES = {
    "EVRP": ("EVRP",),
    "E-CVRP": ("E-CVRP",),
    "EVRPTW": ("EVRPTW",),
    "Nonlinear charging": ("nonlinear",),
    "Capacitated charging stations": ("capacitated charging",),
    "Mixed fleet": ("mixed-fleet", "mixed fleet"),
    "Two-echelon EVRP": ("two-echelon", "two echelon"),
    "V2G / dynamic pricing": ("dynamic pricing", "v2g"),
    "Gradient-aware EVRP": ("gradient", "load dynamics"),
    "Electric DARP": ("dial-a-ride", "darp"),
    "EV-drone routing": ("drone",),
}

def selected_paths(root: Path, dataset_arg: str, instance_mode: str,
                   instance_names: str, max_instances: int):
    all_paths = sorted(p for p in root.rglob("*") if p.is_file()
                       and p.suffix.lower() in {".evrp", ".txt"}
                       and p.name.lower() not in {"readme.txt", "readme.md"})
    requested = [x.strip() for x in dataset_arg.split(",") if x.strip()]
    if not requested or requested == ["all"]:
        selected_datasets = list(DATASET_FOLDER_MAP)
        paths = all_paths
    else:
        selected_datasets = requested
        unknown = sorted(set(requested) - set(DATASET_FOLDER_MAP))
        if unknown:
            raise ValueError(f"Unknown dataset IDs: {', '.join(unknown)}")
        folders = {DATASET_FOLDER_MAP[x] for x in requested}
        paths = [p for p in all_paths if any(folder in p.relative_to(root).as_posix() for folder in folders)]
    if instance_mode == "custom":
        names = {x.strip() for x in instance_names.split(",") if x.strip()}
        if not names:
            raise ValueError("instance_mode=custom requires --instance-names")
        paths = [p for p in paths if p.name in names]
        missing = sorted(names - {p.name for p in paths})
        if missing:
            raise ValueError(f"Requested instance names not found in selected dataset(s): {', '.join(missing)}")
    elif instance_mode == "representative":
        grouped = {}
        for p in paths:
            folder = next((f for f in DATASET_FOLDER_MAP.values() if f in p.relative_to(root).as_posix()), "unknown")
            grouped.setdefault(folder, []).append(p)
        paths = []
        for group in grouped.values():
            paths.extend(group[:1] if len(group) == 1 else [group[0], group[-1]])
    elif instance_mode != "all":
        raise ValueError(f"Unsupported instance_mode: {instance_mode}")
    if max_instances > 0:
        paths = paths[:max_instances]
    return paths, all_paths, selected_datasets

def matches_variant(record: dict, requested_variant: str) -> bool:
    if requested_variant == "all":
        return True
    aliases = VARIANT_ALIASES.get(requested_variant, (requested_variant.lower(),))
    for item in record.get("compatibility", []):
        if item.get("status") not in {"direct_fit", "conditional_fit"}:
            continue
        problem = item.get("problem", "").lower()
        if any(alias.lower() in problem for alias in aliases):
            return True
    # A named source family can be selected even if its parser has not yet been implemented.
    return False

def main():
    ap=argparse.ArgumentParser(description="Inspect selected EVRP benchmark dataset instances.")
    ap.add_argument("--data", default="data/raw")
    ap.add_argument("--out", default="reports")
    ap.add_argument("--dataset", default="all", help="all or comma-separated dataset IDs")
    ap.add_argument("--problem-variant", default="all")
    ap.add_argument("--instance-mode", choices=["all", "representative", "custom"], default="all")
    ap.add_argument("--instance-names", default="", help="Comma-separated exact filenames for custom mode")
    ap.add_argument("--max-instances", type=int, default=0, help="0 means unlimited")
    ap.add_argument("--sample", action="store_true", help="Legacy alias for representative mode")
    ap.add_argument("--fail-on-empty", action="store_true")
    args=ap.parse_args()
    root=Path(args.data); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    mode = "representative" if args.sample else args.instance_mode
    paths, all_paths, selected_datasets = selected_paths(root, args.dataset, mode, args.instance_names, args.max_instances)
    registry_path = Path("data/registry/evrp_dataset_registry.json")
    registry = load_registry(registry_path) if registry_path.exists() else {"datasets": [], "citation_sources": {}}
    raw_records=[attach_provenance(inspect_file(p), p, root, registry) for p in paths]
    records=[x for x in raw_records if matches_variant(x, args.problem_variant)]
    selected_set=set(selected_datasets)
    available_datasets = sorted({
        did for did, folder in DATASET_FOLDER_MAP.items()
        if any(folder in p.relative_to(root).as_posix() for p in all_paths)
    })
    missing_datasets=sorted(selected_set-set(available_datasets))
    summary={
        "files_discovered":len(records),
        "files_available_in_selected_datasets":len(paths),
        "files_available_in_all_local_corpus":len(all_paths),
        "sample_mode":mode=="representative",
        "instance_mode":mode,
        "selected_datasets":selected_datasets,
        "datasets_with_local_files":sorted(selected_set & set(available_datasets)),
        "selected_datasets_without_local_files":missing_datasets,
        "problem_variant":args.problem_variant,
        "max_instances":args.max_instances,
        "passed":sum(x["validation"]["status"]=="passed" for x in records),
        "failed":sum(x["validation"]["status"]=="failed" for x in records),
        "formats":{},
        "filtered_out_by_problem_variant":len(raw_records)-len(records),
    }
    for x in records: summary["formats"][x["format"]]=summary["formats"].get(x["format"],0)+1
    (out/"dataset_report.json").write_text(json.dumps({"summary":summary,"instances":records},indent=2))
    fields=["name","format","dataset_id","dataset_doi","citation_ids","citation_dois","customer_count","station_count","depot_count","vehicles","capacity","energy_capacity","battery_capacity_Q","vehicle_capacity_C","validation_status"]
    with (out/"dataset_summary.csv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore"); w.writeheader()
        for x in records:
            w.writerow({**x, "dataset_id": x.get("provenance",{}).get("dataset_id"), "dataset_doi": x.get("provenance",{}).get("dataset_doi"), "citation_ids": ";".join(x.get("provenance",{}).get("citation_ids",[])), "citation_dois": ";".join(str(z) for z in x.get("provenance",{}).get("citation_dois",[]) if z), "validation_status":x["validation"]["status"]})
    md=["# Dataset inspection report","",f"- Selected dataset(s): **{', '.join(selected_datasets)}**",f"- Problem variant: **{args.problem_variant}**",f"- Instance mode: **{mode}**",f"- Inspected: **{summary['files_discovered']}**",f"- Passed: **{summary['passed']}**",f"- Failed: **{summary['failed']}**",f"- Selected datasets without local raw files: **{', '.join(missing_datasets) or 'None'}**","", "## Formats"]
    md += [f"- `{k}`: {v}" for k,v in sorted(summary["formats"].items())]
    md += ["","## Per-instance validation","", "| Instance | Dataset | Dataset DOI | Paper/data DOI(s) | Format | Validation |","|---|---|---|---|---|---|"]
    for x in records:
        md.append(f"| {x['name']} | {x.get('provenance',{}).get('dataset_id','unmapped')} | {x.get('provenance',{}).get('dataset_doi') or '—'} | {', '.join(str(z) for z in x.get('provenance',{}).get('citation_dois',[]) if z) or '—'} | {x['format']} | {x['validation']['status']} |")
    md += ["","## Compatibility","", "Compatibility labels are data-capability assessments, not route feasibility or solver certificates.", ""]
    for x in records:
        md += [f"### {x['name']}"]
        md += [f"- **{c['problem']} — {c['status']}**: {c['reason']}" for c in x["compatibility"]]
    (out/"dataset_report.md").write_text("\n".join(md))
    (out/"source_registry_snapshot.json").write_text(json.dumps(registry, indent=2, ensure_ascii=False))
    print(json.dumps(summary,indent=2))
    if summary["failed"] or (args.fail_on_empty and not records): sys.exit(1)
if __name__=="__main__": main()
