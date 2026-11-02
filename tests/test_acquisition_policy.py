import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_all_missing_sources_have_source_specific_acquisition_adapters():
    config = json.loads((ROOT / "acquisition/sources.json").read_text())
    sources = config["sources"]
    assert set(sources) == {f"EVRP-{i:03d}" for i in range(3, 16)}
    supported = {"vrp_rep", "dimacs_derived", "mendeley", "zenodo", "dryad", "github"}
    assert {s["adapter"] for s in sources.values()} <= supported
    for dataset_id, source in sources.items():
        assert source["source_url"].startswith("https://")
        assert source["license_evidence_url"].startswith("https://")
        assert source["destination"].startswith("data/raw/")


def test_automatic_commit_is_limited_to_explicitly_licensed_sources():
    config = json.loads((ROOT / "acquisition/sources.json").read_text())
    sources = config["sources"]
    eligible = {did for did, item in sources.items() if item["redistribute"]}
    assert eligible == {"EVRP-005", "EVRP-008", "EVRP-009", "EVRP-010", "EVRP-012", "EVRP-014"}
    for did, item in sources.items():
        if item["license_gate"] == "manual_review":
            assert item["redistribute"] is False
        if item["redistribute"]:
            assert item["license_gate"] == "verified"
            assert item["license_spdx"] in {"CC-BY-4.0", "CC0-1.0"}


def test_acquisition_workflow_is_manual_and_one_dataset_per_run():
    workflow = (ROOT / ".github/workflows/dataset-acquisition.yml").read_text()
    assert "workflow_dispatch:" in workflow
    assert "schedule:" not in workflow
    assert "push:" not in workflow
    assert "EVRP-003" in workflow and "EVRP-015" in workflow
    assert "peter-evans/create-pull-request" in workflow
    assert "acquisition-failure" in workflow
    assert "licensing-review" in workflow


def test_parser_validation_scope_remains_separate_from_acquisition():
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from evrp_bench.runner import PARSER_ENABLED_DATASETS
    assert PARSER_ENABLED_DATASETS == {"EVRP-001", "EVRP-002"}


def test_archive_extractor_rejects_path_traversal(tmp_path):
    import importlib.util
    import zipfile
    import pytest
    module_path = ROOT / "scripts/acquire_dataset.py"
    spec = importlib.util.spec_from_file_location("evrp_acquire", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    archive = tmp_path / "unsafe.zip"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("../outside.txt", "must not escape")
    with pytest.raises(module.AcquisitionError):
        module.safe_extract_zip(archive, tmp_path / "extracted")
    assert not (tmp_path / "outside.txt").exists()
