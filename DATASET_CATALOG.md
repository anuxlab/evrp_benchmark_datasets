# EVRP benchmark dataset catalogue

**15 curated source collections | 2 locally integrated datasets | 109 locally parser-validated instances**

Catalogued does not mean downloaded. The 15 folders each contain a source-specific README and machine-readable dataset card. Only EVRP-001 and EVRP-002 currently contain raw instance files in this repository snapshot. See `data/acquisition_status.csv` for authoritative local status.

| ID | Collection | Published/expected count | Local files | Problem family | Source |
| EVRP-001 | Mavrovouniotis E-CVRP benchmark (current upstream listing) | 24 | 17 | E-CVRP, load-dependent energy E-CVRP | [Source](https://github.com/Mavrovouniotis/e-cvrp_benchmark_instances) |
| EVRP-002 | Schneider-Goeke E-VRPTW instances | 92 | 92 | E-VRPTW, E-CVRPTW | [Source](https://data.mendeley.com/datasets/h3mrm5dhxw/1) |
| EVRP-003 | Montoya et al. nonlinear charging benchmark | 120 | 0 | E-VRP-NL | [Source](https://www.vrp-rep.org/datasets/item/2016-0020.html) |
| EVRP-004 | Froger capacitated charging-station variants | 240 | 0 | E-VRP-NL-C, capacitated charging stations | [Source](https://dimacs.rutgers.edu/programs/implementation-challenges/vehicle-routing/implementation-challenge-vehicle-routing/electric-vehicle-routing-problem) |
| EVRP-005 | Goeke-Schneider mixed-fleet EVRPTW-MF | Not recorded | 0 | EVRPTW-MF, mixed electric/ICE fleet | [Source](https://data.mendeley.com/datasets/bd7rm5fw6k/1) |
| EVRP-006 | Felipe et al. GVRP multiple technologies and partial recharges | 41 | 0 | GVRP-MTPR, multiple charging technologies, partial recharge | [Source](https://www.vrp-rep.org/datasets/item/2018-0004.html) |
| EVRP-007 | Akbay et al. expanded two-echelon EVRP dataset | 3000 | 0 | 2E-EVRP, 2E-EVRPTW, SPD, partial delivery | [Source](https://zenodo.org/records/14844216) |
| EVRP-008 | V2G and dynamic energy pricing extended EVRPTW | Not recorded | 0 | EVRPTW-V2G, time-of-use energy pricing | [Source](https://data.mendeley.com/datasets/dmnhggw478/1) |
| EVRP-009 | Gradient-aware EVRPTW with altitude information | Not recorded | 0 | EVRPTW-GR, gradient/load-dependent energy, regenerative braking | [Source](https://data.mendeley.com/datasets/srfdbp2twv/1) |
| EVRP-010 | Charging-station energy differences | Not recorded | 0 | EVRP heterogeneous station energy | [Source](https://data.mendeley.com/datasets/4ktbt29z5x/1) |
| EVRP-011 | EVRP with backhauls and time windows under uncertainty (EVRPBTW-USUT) | 60 | 0 | EVRPBTW-USUT, backhauls, time windows, uncertain travel/service times | [Source](https://datadryad.org/dataset/doi:10.5061/dryad.6hdr7srbv) |
| EVRP-012 | Mixed-fleet VRP with low-emission zones (EVRPTW-derived + Milan case) | Not recorded | 0 | mixed-fleet EVRP, low-emission-zone routing, real-road case study | [Source](https://data.mendeley.com/datasets/np452gmj7f/2) |
| EVRP-013 | Electric autonomous dial-a-ride benchmark (adjacent family) | Not recorded | 0 | eADARP, electric dial-a-ride, ride-pooling | [Source](https://github.com/claudiabongiovanni/eADARP) |
| EVRP-014 | Electric vehicle-drone routing instances (adjacent family) | 128 | 0 | EV-drone routing, synchronised truck-drone routing | [Source](https://github.com/setyotw/EVDRP_instances) |
| EVRP-015 | EM-DARP electric shuttle demand-responsive routing dataset (adjacent family) | Not recorded | 0 | electric mobility DARP, electric shuttle routing, demand-responsive transport | [Source](https://zenodo.org/records/23468137) |

## Per-dataset documentation

Open the `README.md` in each corresponding folder under `data/raw/`. Each README describes parameters, intended use cases, problem compatibility, acquisition status, citation and validation instructions.

## Interpretation of instance counts

- **EVRP-001:** 17 files in the uploaded historical/local snapshot. The current upstream repository listing was separately recorded as 24; do not conflate the snapshots.
- **EVRP-002:** 92 files from the supplied Mendeley Data version 1 archive.
- **EVRP-003 / EVRP-004:** 120 Montoya base instances and 240 Froger/DIMACS capacitated-station variants are source-reported counts; they are not locally downloaded here.
- Other published counts are as recorded in the source registry and should be rechecked against the pinned release before a new experiment.

## Source records and citations

The machine-readable registry includes publication citation IDs and DOI metadata. Consult `references.bib` and `docs/CITATION_AND_PROVENANCE.md`.
