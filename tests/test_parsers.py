from pathlib import Path
from evrp_bench.runner import inspect_file

ROOT=Path(__file__).resolve().parents[1]

def test_uploaded_evrp_sample():
    p=ROOT/"data/raw/mavrovouniotis-upload/E-n22-k4.evrp"
    r=inspect_file(p)
    assert r["format"]=="mavrovouniotis_evrp"
    assert r["validation"]["status"]=="passed"
    assert r["energy_capacity"]==94
    assert r["capacity"]==6000
    assert len(r["stations"])==8

def test_uploaded_evrptw_sample():
    p=ROOT/"data/raw/mendeley-evrptw/evrptw_instances/c101C10.txt"
    r=inspect_file(p)
    assert r["format"]=="schneider_evrptw_tabular"
    assert r["validation"]["status"]=="passed"
    assert r["customer_count"]>0
    assert r["battery_capacity_Q"] is not None
    assert r["has_time_windows"] is True
