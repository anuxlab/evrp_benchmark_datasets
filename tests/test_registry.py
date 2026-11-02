import json
from pathlib import Path
from evrp_bench.registry import load_registry, validate_registry
ROOT = Path(__file__).resolve().parents[1]

def test_registry_has_traceable_publication_links():
    reg = load_registry(ROOT / "data/registry/evrp_dataset_registry.json")
    assert len(reg["datasets"]) >= 10
    assert validate_registry(reg) == []

def test_every_dataset_has_citation_or_explicitly_no_publication():
    reg = load_registry(ROOT / "data/registry/evrp_dataset_registry.json")
    for ds in reg["datasets"]:
        assert isinstance(ds["related_citation_ids"], list)
        assert ds["official_source_url"].startswith("https://")
