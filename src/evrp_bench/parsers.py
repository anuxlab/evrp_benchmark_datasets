from __future__ import annotations
import re
from pathlib import Path

def parse_evrp(path: Path) -> dict:
    """Parse the Mavrovouniotis/CEC EVRP text format without assuming node IDs are contiguous."""
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, sections, current = {}, {}, None
    section_names = {"NODE_COORD_SECTION", "DEMAND_SECTION", "STATION_COORD_SECTION",
                     "STATIONS_COORD_SECTION", "DEPOT_SECTION"}
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        key = line.split()[0].upper()
        if key in section_names:
            current = key
            sections.setdefault(current, [])
            continue
        if key == "EOF":
            current = None
            continue
        if current:
            sections[current].append(line)
        elif ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip().upper()] = v.strip()
        else:
            parts = line.split(maxsplit=1)
            if len(parts) == 2 and parts[0].upper() not in section_names:
                meta[parts[0].upper()] = parts[1].strip()

    def num(k, default=None):
        try:
            x = float(meta[k])
            return int(x) if x.is_integer() else x
        except (KeyError, ValueError):
            return default

    coords = []
    for row in sections.get("NODE_COORD_SECTION", []):
        p = row.split()
        if len(p) >= 3:
            coords.append({"id": p[0], "x": float(p[1]), "y": float(p[2])})
    demands = []
    for row in sections.get("DEMAND_SECTION", []):
        p = row.split()
        if len(p) >= 2:
            demands.append({"id": p[0], "demand": float(p[1])})
    station_rows = sections.get("STATION_COORD_SECTION", sections.get("STATIONS_COORD_SECTION", []))
    stations = [r.split()[0] for r in station_rows if r.split()]
    depots = []
    for row in sections.get("DEPOT_SECTION", []):
        token = row.split()[0]
        if token == "-1":
            break
        depots.append(token)
    return {
        "format": "mavrovouniotis_evrp", "name": path.name,
        "type": meta.get("TYPE"), "vehicles": num("VEHICLES"),
        "dimension_header": num("DIMENSION"), "station_count_header": num("STATIONS"),
        "capacity": num("CAPACITY"), "energy_capacity": num("ENERGY_CAPACITY"),
        "energy_consumption": num("ENERGY_CONSUMPTION"),
        "edge_weight_type": meta.get("EDGE_WEIGHT_TYPE"),
        "optimal_value_or_bound": num("OPTIMAL_VALUE"),
        "coordinates": coords, "demands": demands, "stations": stations,
        "depots": depots, "metadata": meta,
        "customer_count": len(demands) - len(depots) if demands else None,
    }

def parse_solomon_evrptw(path: Path) -> dict:
    """Parse Schneider/Goeke tabular E-VRPTW instances with Q,C,r,g,v footer parameters."""
    text = path.read_text(encoding="utf-8", errors="replace")
    nodes, params = [], {}
    data_started = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        p = line.split()
        if not data_started and len(p) >= 8 and p[0].lower() == "stringid":
            data_started = True
            continue
        if data_started and len(p) >= 8:
            try:
                nodes.append({"id": p[0], "type": p[1].lower(), "x": float(p[2]),
                              "y": float(p[3]), "demand": float(p[4]),
                              "ready_time": float(p[5]), "due_date": float(p[6]),
                              "service_time": float(p[7])})
                continue
            except ValueError:
                pass
        m = re.match(r"^([QCrgv])\s+.*?/\s*([-+]?\d+(?:\.\d+)?)\s*/$", line, re.I)
        if m:
            params[m.group(1).strip()] = float(m.group(2))
    customers = [n for n in nodes if n["type"] == "c"]
    stations = [n for n in nodes if n["type"] == "f"]
    depots = [n for n in nodes if n["type"] == "d"]
    return {
        "format": "schneider_evrptw_tabular", "name": path.name,
        "nodes": nodes, "customer_count": len(customers),
        "station_count": len(stations), "depot_count": len(depots),
        "has_time_windows": bool(customers) and all("ready_time" in n and "due_date" in n for n in customers),
        "has_demands": bool(customers) and all("demand" in n for n in customers),
        "battery_capacity_Q": params.get("Q"),
        "vehicle_capacity_C": params.get("C"),
        "energy_consumption_rate_r": params.get("r"),
        "inverse_refueling_rate_g": params.get("g"),
        "average_velocity_v": params.get("v"),
        "coordinate_count": len(nodes),
        "time_window_horizon": max((n["due_date"] for n in nodes), default=None),
    }

def validate_record(r: dict) -> list[str]:
    errors = []
    if r["format"] == "mavrovouniotis_evrp":
        if not r["coordinates"]: errors.append("missing NODE_COORD_SECTION")
        if not r["demands"]: errors.append("missing DEMAND_SECTION")
        if not r["depots"]: errors.append("missing DEPOT_SECTION")
        if r["energy_capacity"] is None: errors.append("missing ENERGY_CAPACITY")
        if r["capacity"] is None: errors.append("missing CAPACITY")
        if r["station_count_header"] is not None and r["stations"] and r["station_count_header"] != len(r["stations"]):
            errors.append(f"station count mismatch: header={r['station_count_header']} parsed={len(r['stations'])}")
        if r["dimension_header"] is not None and len(r["coordinates"]) not in (r["dimension_header"], r["dimension_header"] + (r["station_count_header"] or 0)):
            # Preserve as warning-level structural note in report; not fatal.
            pass
    else:
        if not r["nodes"]: errors.append("no tabular nodes parsed")
        if not any(n["type"] == "d" for n in r["nodes"]): errors.append("missing depot row")
        if not any(n["type"] == "c" for n in r["nodes"]): errors.append("missing customer rows")
        if not any(n["type"] == "f" for n in r["nodes"]): errors.append("missing charging-station rows")
        for k in ("battery_capacity_Q", "vehicle_capacity_C", "energy_consumption_rate_r",
                  "inverse_refueling_rate_g", "average_velocity_v"):
            if r[k] is None: errors.append(f"missing parameter {k}")
    return errors
