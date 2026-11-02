# Schneider–Goeke EVRPTW benchmark instances (Mendeley Data v1)

**Dataset ID:** `EVRP-002` · **92 local instances parser-validated**

## Source and scientific provenance

- Dataset: [Mendeley Data, h3mrm5dhxw, Version 1](https://data.mendeley.com/datasets/h3mrm5dhxw/1)
- Dataset DOI: `10.17632/h3mrm5dhxw.1`
- Primary paper: Schneider, M., Stenger, A., & Goeke, D. (2014). *The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations*. Transportation Science, 48(4), 500–520.
- Paper DOI: https://doi.org/10.1287/trsc.2013.0490
- Licence: CC BY-NC 3.0 as recorded for the supplied Mendeley release. Attribution is required; non-commercial restriction means do not assume commercial reuse or redistribution is allowed.

## What this dataset represents

This benchmark extends vehicle routing with customer time windows to electric vehicles and recharging stations. It supports EVRPTW experiments with a single depot, delivery demands, charging-station visits and battery/energy constraints.

The supplied archive contains 92 `.txt` instance files under `evrptw_instances/`. These are preserved as received. The runner inspected all 92 files and passed its current structural parser checks.

## File structure

```text
mendeley-evrptw/
├── README.md
└── evrptw_instances/
    ├── c101_21.txt
    ├── c101C5.txt
    ├── c101C10.txt
    ├── ...
```

Filename families follow Solomon-style spatial patterns:

- `C`: clustered customer distributions.
- `R`: randomly distributed customer locations.
- `RC`: mixed random and clustered distributions.
- Numeric family identifiers (e.g. 101, 201) identify source instance groups.
- Additional suffixes such as `_21`, `C5`, `C10`, `C15` are retained exactly as supplied. Do not infer charging-station counts solely from a filename suffix; parse the actual station rows in each file.

## Node record format

The file begins with a tabular header:

```text
StringID   Type   x   y   demand   ReadyTime   DueDate   ServiceTime
```

| Field | Meaning | Unit / caution |
|---|---|---|
| `StringID` | Unique node identifier (e.g. D0, S0, C98) | String; do not cast to integer |
| `Type` | Node class: `d` depot, `f` charging facility, `c` customer | Categorical |
| `x`, `y` | Cartesian coordinates | Source coordinate units; not automatically kilometres |
| `demand` | Customer delivery demand | Source load units |
| `ReadyTime` | Earliest service time | Source time units |
| `DueDate` | Latest permitted service time / time-window bound | Confirm exact service-start semantics against the paper |
| `ServiceTime` | Service duration at node | Source time units |

The depot and charging-station rows are generally represented with zero demand. Their time-window/service fields may be populated for parser uniformity.

## Vehicle and energy footer parameters

The source files append scalar parameters in slash-delimited records:

```text
Q Vehicle fuel tank capacity /77.75/
C Vehicle load capacity /200.0/
r fuel consumption rate /1.0/
g inverse refueling rate /3.47/
v average Velocity /1.0/
```

| Symbol | Parser field | Meaning | Caution |
|---|---|---|---|
| `Q` | `battery_capacity_Q` | Maximum battery/fuel-tank energy capacity | Preserve source unit |
| `C` | `vehicle_capacity_C` | Vehicle payload capacity | Source load unit |
| `r` | `energy_consumption_rate_r` | Energy consumption rate | Apply source's distance/energy convention |
| `g` | `inverse_refueling_rate_g` | Inverse refuelling/charging rate | Used to convert energy amount into charging time under the source model |
| `v` | `average_velocity_v` | Average travel velocity | Coordinate-distance and time units must be consistent |

Do not assume that Q/r/g/v are dimensionally interchangeable with parameters from other EVRP datasets. The canonical schema must store the original symbol, source unit, normalized field, unit conversion and provenance.

## Problem eligibility

| Problem | Eligibility | Reason |
|---|---|---|
| EVRPTW | Direct fit | Customer time windows, service times, depot, charging stations, demand and energy parameters |
| EVRP | Direct fit after explicitly relaxing time windows | All core electric routing fields are represented |
| E-CVRP | Direct fit | Demand and payload capacity are represented |
| Partial charging | Conditional | Charging policy/amount decisions must be specified consistently with the paper |
| Dynamic electricity prices / V2G | Conditional derived experiment only | Add external tariff or grid-export data; not present in original files |
| Nonlinear charging | Unsupported by original parameterization | `g` is a scalar inverse rate, not a nonlinear charging curve |
| Heterogeneous fleet | Unsupported | Per-vehicle type parameters are not represented |
| Multi-depot / pickup-delivery / two-echelon | Unsupported | Required structural fields are absent |

Eligibility is about data attributes, not a claim that an arbitrary solver formulation can be tested without additional modelling.

## How to use

From repository root:

```bash
# Validate all locally integrated datasets
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports --dataset EVRP-002

# Select a particular file
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports \
  --dataset EVRP-002 --instance-mode custom \
  --instance-names "c101C10.txt"

# Inspect representative examples
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports \
  --dataset EVRP-002 --instance-mode representative
```

## Citation

Cite both the dataset and the paper:

> Schneider, M., Stenger, A., & Goeke, D. (2014). The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations. *Transportation Science*, 48(4), 500–520. https://doi.org/10.1287/trsc.2013.0490

> Schneider, M., Stenger, A., & Goeke, D. (2014). *EVRPTW benchmark instances* (Version 1) [Data set]. Mendeley Data. https://doi.org/10.17632/h3mrm5dhxw.1

Also cite this repository if you used its registry, parsers or curated benchmark interface; copy-ready APA/IEEE/BibTeX/Chicago references are in `docs/CITATION_AND_PROVENANCE.md`.
