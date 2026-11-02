from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def test_every_registered_dataset_has_folder_readme_and_card():
    registry = json.loads((ROOT / "data/registry/evrp_dataset_registry.json").read_text())
    for ds in registry["datasets"]:
        folder = ROOT / ds["repository_folder"]
        assert folder.is_dir(), ds["dataset_id"]
        assert (folder / "README.md").is_file(), ds["dataset_id"]
        assert (folder / "dataset.json").is_file(), ds["dataset_id"]

def test_catalogue_and_local_integration_counts_are_distinct():
    registry = json.loads((ROOT / "data/registry/evrp_dataset_registry.json").read_text())
    assert len(registry["datasets"]) == 15
    integrated = [d for d in registry["datasets"] if d["local_status"] in {
        "locally_ingested_and_parser_validated", "acquired_and_schema_validated"
    }]
    assert len(integrated) >= 2
    parser_validated = [d for d in integrated if d["local_status"] == "locally_ingested_and_parser_validated"]
    assert sum(d["local_instance_count"] for d in parser_validated) >= 109
