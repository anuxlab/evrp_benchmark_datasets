from pathlib import Path
from evrp_bench.runner import selected_paths, inspect_file, matches_variant, attach_provenance
from evrp_bench.registry import load_registry

ROOT = Path(__file__).resolve().parents[1]

def test_dataset_selection_returns_only_selected_dataset():
    paths, _, selected = selected_paths(ROOT/"data/raw", "EVRP-001", "all", "", 0)
    assert selected == ["EVRP-001"]
    assert len(paths) == 17
    assert all(p.suffix == ".evrp" for p in paths)

def test_representative_mode_is_two_per_local_dataset():
    paths, _, _ = selected_paths(ROOT/"data/raw", "all", "representative", "", 0)
    assert len(paths) == 4

def test_custom_instance_selection():
    paths, _, _ = selected_paths(ROOT/"data/raw", "EVRP-001", "custom", "E-n22-k4.evrp", 0)
    assert [p.name for p in paths] == ["E-n22-k4.evrp"]

def test_problem_variant_filter_uses_compatibility():
    rec = inspect_file(ROOT/"data/raw/mavrovouniotis-upload/E-n22-k4.evrp")
    assert matches_variant(rec, "E-CVRP")
    assert not matches_variant(rec, "EVRPTW")
