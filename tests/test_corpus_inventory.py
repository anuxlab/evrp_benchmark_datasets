from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_uploaded_corpus_inventory():
    evrp = list((ROOT/"data/raw/mavrovouniotis-upload").glob("*.evrp"))
    evrptw = [p for p in (ROOT/"data/raw/mendeley-evrptw/evrptw_instances").glob("*.txt")
              if p.name.lower() != "readme.txt"]
    assert len(evrp) == 17
    assert len(evrptw) == 92

def test_all_local_instances_resolve_to_registered_dataset():
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from evrp_bench.runner import attach_provenance, inspect_file
    from evrp_bench.registry import load_registry
    registry = load_registry(ROOT / "data/registry/evrp_dataset_registry.json")
    raw = ROOT / "data/raw"
    from evrp_bench.runner import parser_input_paths
    paths = parser_input_paths(raw)
    for path in paths:
        rec = attach_provenance(inspect_file(path), path, raw, registry)
        assert rec["provenance"]["dataset_id"] in {"EVRP-001", "EVRP-002"}
        assert rec["provenance"]["citation_ids"]


def test_sample_mode_selects_two_examples_per_format():
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from evrp_bench.runner import select_input_paths
    sample = select_input_paths(ROOT / "data/raw", sample=True)
    assert len(sample) == 4
    assert sum(p.suffix.lower() == ".evrp" for p in sample) == 2
    assert sum(p.suffix.lower() == ".txt" for p in sample) == 2
