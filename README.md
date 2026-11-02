# EVRP Benchmark Lab

**A source-aware, research-oriented catalogue and validation pipeline for diversified Electric Vehicle Routing Problem (EVRP) benchmark instances.**

The repository is intended for researchers and practitioners comparing routing formulations and algorithms across classical EVRP, time windows, nonlinear/partial charging, charger capacity, mixed fleets, load/gradient-dependent energy, dynamic pricing/V2G, two-echelon logistics and adjacent electric mobility problems.

> **Current scope:** dataset registry, provenance/citation checks, parsing and smoke tests for the two user-supplied corpora. External datasets are catalogued with official links and citations, but are not claimed as downloaded or locally validated until an adapter and archive-level test are added. No optimization algorithms or solution feasibility claims are included yet.

## Start here

- [Dataset catalogue](DATASET_CATALOG.md)
- [Machine-readable registry](data/registry/evrp_dataset_registry.json)
- [Problem taxonomy and eligibility](docs/PROBLEM_TAXONOMY.md)
- [Citation and provenance policy](docs/CITATION_AND_PROVENANCE.md)
- [Parameter dictionary](docs/DATA_DICTIONARY.md)
- [Roadmap](docs/ROADMAP.md)
- [Initial parser validation](INITIAL_VALIDATION.md)

## What is catalogued?

The registry includes 15 source records spanning Mavrovouniotis E-CVRP, Schneider-Goeke E-VRPTW, Montoya nonlinear charging, Froger/DIMACS capacitated charging variants, Goeke-Schneider mixed fleet, Felipe multiple charging technologies/partial recharge, Akbay two-echelon EVRP, dynamic pricing/V2G, gradient-aware EVRPTW, station energy heterogeneity, uncertain backhaul EVRP, low-emission-zone mixed fleet, electric dial-a-ride, EV-drone routing and electric-shuttle DARP. See each record for publication links, source version, parameters, licence status and compatibility caveats.

## Locally ingested snapshots

- `data/raw/mavrovouniotis-upload/`: 17 `.evrp` files supplied by the user. This is a distinct historical/uploaded snapshot, not the current upstream GitHub listing (24 `.evrp` instances observed in the current repository listing).
- `data/raw/mendeley-evrptw/evrptw_instances/`: 92 `.txt` instance files supplied from Mendeley Data version 1.

Raw snapshots are preserved. Do not overwrite or rename source files to make them appear to belong to another release. `data/manifest.json` stores file sizes and SHA-256 checksums.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip pytest
PYTHONPATH=src pytest -q
PYTHONPATH=src python -m evrp_bench.runner --data data/raw --out reports
```

## GitHub Actions

`.github/workflows/dataset-smoke-tests.yml` is manually triggered only (`workflow_dispatch`); there is no push or pull-request trigger. It validates tests, the source registry and optionally all locally committed instances. It uploads reports as workflow artifacts. It does not install optimization solvers or download unreviewed third-party archives.

## Trust and compatibility labels

- `direct_fit`: required problem attributes are present in the documented dataset schema.
- `conditional_fit`: usable only after an explicit transformation or assumption (e.g., relaxing time windows).
- `candidate_direct`: source description indicates the feature, but the files/units have not yet been inspected.
- `unsupported`: required fields or structural features are absent.
- `not_applicable`: related but distinct problem family (e.g., dial-a-ride rather than freight EVRP).

A parser pass only proves that the implemented parser could read required structural fields. It does not prove mathematical feasibility, route feasibility, optimality, or full scientific suitability.

## Citation rule

Every experiment must cite both (1) the exact dataset version/DOI or pinned repository commit and (2) the primary paper defining the benchmark/problem. For a derived benchmark, cite its extension paper and the parent dataset paper. Follow [docs/CITATION_AND_PROVENANCE.md](docs/CITATION_AND_PROVENANCE.md).

## Data licensing

Publicly downloadable does not mean freely redistributable. Third-party corpora are external references by default. For example, the Schneider-Goeke Mendeley dataset is marked CC BY-NC 3.0; do not assume commercial redistribution rights. Review every exact version's licence before vendoring it.

## Project status

See [Roadmap](docs/ROADMAP.md). The next priority is controlled ingestion and adapters for Montoya/Froger, mixed-fleet, Felipe, 2E-EVRP, dynamic-price/V2G and gradient-aware datasets, followed by a canonical schema and mathematical validation.
