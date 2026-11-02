from __future__ import annotations
import json
from pathlib import Path

REQUIRED_DATASET_FIELDS = {"dataset_id", "name", "official_source_url", "problem_families", "key_parameters", "recommended_use_cases", "compatibility", "provenance_status", "licence_status", "related_citation_ids"}

def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def validate_registry(registry: dict) -> list[str]:
    errors = []
    citations = registry.get("citation_sources", {})
    seen = set()
    for ds in registry.get("datasets", []):
        missing = REQUIRED_DATASET_FIELDS - set(ds)
        if missing:
            errors.append(f"{ds.get('dataset_id', '<unknown>')}: missing fields {sorted(missing)}")
        did = ds.get("dataset_id")
        if did in seen:
            errors.append(f"duplicate dataset_id: {did}")
        seen.add(did)
        if not str(ds.get("official_source_url", "")).startswith(("https://", "http://")):
            errors.append(f"{did}: invalid official_source_url")
        for cid in ds.get("related_citation_ids", []):
            if cid not in citations:
                errors.append(f"{did}: unknown related citation id {cid}")
        if not ds.get("problem_families"):
            errors.append(f"{did}: problem_families must not be empty")
    return errors
