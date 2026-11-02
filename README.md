# EVRP Benchmark Datasets

[![Catalogued collections](https://img.shields.io/badge/catalogued%20collections-15-2563eb)](DATASET_CATALOG.md)
[![Locally integrated](https://img.shields.io/badge/locally%20integrated-2-16a34a)](data/registry/evrp_dataset_registry.json)
[![Locally validated instances](https://img.shields.io/badge/instances%20validated-109-16a34a)](reports/dataset_summary.csv)
[![Validation](https://img.shields.io/badge/CI-manual%20%2B%20PR-0f766e)](.github/workflows/)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/code%20license-MIT-yellow.svg)](LICENSE)

**A provenance-first, research-oriented collection of Electric Vehicle Routing Problem (EVRP) benchmark sources, instance files, dataset documentation, and reproducible validation workflows.**

The goal is to help researchers and practitioners evaluate algorithms across diverse routing formulations—not to present unrelated problem variants as if they were interchangeable.

> **Corpus status (2 November 2026):** 15 curated source collections are catalogued (12 freight EVRP/VRP variants and 3 adjacent electric-mobility families). Two collections currently have raw files locally integrated: 17 Mavrovouniotis-uploaded `.evrp` instances and 92 Schneider/Goeke EVRPTW `.txt` instances, for **109 parser-validated local instances**. The other 13 source folders contain source-specific READMEs and acquisition instructions, but are not falsely counted as locally downloaded data.

## At a glance

| Metric | Current count | Meaning |
|---|---:|---|
| Curated source collections | **15** | Research/official source records with citations and problem-family metadata |
| Locally integrated datasets | **2** | Actual raw files present in this repository snapshot |
| Parser-validated instances | **109** | 17 `.evrp` + 92 EVRPTW `.txt` files |
| Parser-level passes in supplied runner | **109 / 109** | Structural parsing only; not mathematical feasibility or optimality |
| Additional source folders | **13** | README, metadata and acquisition/licence instructions; files not yet ingested |

Counts are generated from the current registry and validation snapshot. They will change only after a source release has been acquired, licence-reviewed, checksummed, parsed and validated.

## Benchmark diversity

The catalogue covers:

- Classical EVRP / E-CVRP and load-dependent energy
- EVRPTW and mixed electric/conventional fleets
- Nonlinear charging and capacitated charging stations
- Multiple charging technologies and partial recharging
- Two-echelon EVRP
- Dynamic electricity prices and vehicle-to-grid (V2G)
- Road-gradient and load-dependent energy
- Backhauls and uncertain travel/service conditions
- Low-emission-zone routing
- Adjacent electric dial-a-ride, EV-drone routing and electric shuttle DARP

See [Dataset catalogue](DATASET_CATALOG.md) and [Problem taxonomy](docs/PROBLEM_TAXONOMY.md).

## Repository layout

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       ├── dataset-smoke-tests.yml
│       ├── custom-benchmark-validation.yml
│       ├── dataset-acquisition.yml
│       └── pr-validation.yml
├── acquisition/
│   ├── sources.json                 # 13 source-specific adapters and licence gates
│   └── README.md
├── scripts/acquire_dataset.py       # source download, integrity checks and PR staging
├── data/
│   ├── raw/                         # source folders; only validated acquisitions are committed
│   ├── registry/evrp_dataset_registry.json
│   ├── acquisition_status.csv
│   └── manifest.json
├── docs/
│   ├── CITATION_AND_PROVENANCE.md
│   ├── CONTRIBUTING.md
│   ├── DATA_DICTIONARY.md
│   ├── PROBLEM_TAXONOMY.md
│   └── RUNNER_LOGS_AND_ARTIFACTS.md
├── artifacts/
│   ├── runner_logs/                 # supplied full runner log export
│   └── runner_reports/              # supplied JSON/CSV/Markdown report snapshot
├── reports/                         # current local validation reports
├── src/evrp_bench/                  # parsers, registry, compatibility and runner
└── tests/
```

## Start here

1. Read the dataset-specific `README.md` inside the corresponding `data/raw/<dataset-folder>/`.
2. Check [DATASET_CATALOG.md](DATASET_CATALOG.md) for source links, DOI, publication, use cases and eligibility.
3. Check [data/registry/evrp_dataset_registry.json](data/registry/evrp_dataset_registry.json) for machine-readable metadata.
4. Review [data/acquisition_status.csv](data/acquisition_status.csv) before assuming a dataset is locally available.
5. Read [citation and provenance rules](docs/CITATION_AND_PROVENANCE.md) before publishing results.

## Local installation and validation

```bash
git clone https://github.com/anuxlab/evrp_benchmark_datasets.git
cd evrp_benchmark_datasets

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"

# Unit tests and registry checks
PYTHONPATH=src pytest -vv

# All currently local instances
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports \
  --dataset all --problem-variant all --instance-mode all

# One source collection
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports --dataset EVRP-001

# Representative samples from all locally integrated collections
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports --dataset all --instance-mode representative

# Exact instance selection
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports --dataset EVRP-001 \
  --instance-mode custom --instance-names "E-n22-k4.evrp"
```

## GitHub Actions

All workflows retain manual execution for benchmark runs. The repository additionally runs lightweight pull-request checks.

### 1. Smoke test

`.github/workflows/dataset-smoke-tests.yml`

- Run all local files or representative examples.
- Check parser and registry integrity.
- Upload JSON, CSV, Markdown reports and runner logs.

### 2. Custom benchmark validation

`.github/workflows/custom-benchmark-validation.yml`

Open **Actions → Custom EVRP benchmark validation → Run workflow**. The form provides:

| Input | Choices / purpose |
|---|---|
| Dataset | `all` or a registered dataset ID (`EVRP-001` … `EVRP-015`) |
| Problem variant | `all`, EVRP, E-CVRP, EVRPTW, nonlinear charging, capacitated stations, mixed fleet, 2E-EVRP, V2G, gradient, DARP, EV-drone |
| Instance mode | `all`, `representative`, `custom` |
| Instance names | Exact comma-separated filenames for custom mode |
| Max instances | `0` for unlimited, otherwise a positive cap |
| Validation level | `quick`, `standard`, `strict` |
| Fail on empty | Fail if no matching local instance exists |

**GitHub limitation:** `workflow_dispatch` choice options are static YAML values; GitHub does not populate dropdown choices dynamically from the registry. The exact per-dataset instance list is therefore provided by `custom` filename input, with all/representative shortcuts.

A selected dataset with no local files is reported as *catalogued but not ingested*. It is not silently downloaded or counted as tested.

### 3. Dataset acquisition

`.github/workflows/dataset-acquisition.yml`

Open **Actions → Dataset acquisition → Run workflow** and select one missing collection (`EVRP-003` … `EVRP-015`) per run. The runner uses a source-specific adapter (VRP-REP, Mendeley, Zenodo, Dryad, GitHub, or the DIMACS derived-set specification), downloads to an ephemeral staging directory, checks archive safety and file integrity, and records SHA-256 checksums.

- Licence-cleared sources are copied into their `data/raw/` folder and submitted as a pull request. The workflow never pushes directly to `main`. It runs the repository test suite before opening a PR. To have the generated PR also trigger the normal `pull_request` workflow, optionally configure a fine-grained `GH_PR_TOKEN` secret; otherwise the default `GITHUB_TOKEN` event-suppression rules may prevent that follow-up workflow from firing.
- Sources with unclear or restrictive redistribution terms are not committed. The runner uploads the report and opens a `licensing-review` issue.
- Download or validation failures open a detailed `acquisition-failure` issue with source, run, error and artifact references.
- README integrated-collection counts are updated only after a licence-cleared acquisition passes structural validation. Parser-validated instance counts remain unchanged until a dataset-specific parser passes.

See [acquisition adapters and source-by-source licence policy](acquisition/README.md) and [the acquisition policy](docs/DATASET_ACQUISITION.md).

### 4. Pull-request checks

`pr-validation.yml` runs tests, registry checks and corpus inventory validation for proposed changes. It does not run optimization solvers.

### Failure triage

When a manual validation workflow fails, it creates a GitHub Issue with labels `datasets`, `ci-failure`, and `workflow-failure`. Runner output and inspection reports are uploaded even on failure. See [runner logs and artifacts](docs/RUNNER_LOGS_AND_ARTIFACTS.md).

## Compatibility and scientific validity

`direct_fit`, `conditional_fit`, `candidate_direct`, `unsupported` and `not_applicable` are dataset-capability assessments. A parser pass means only that the implemented parser could read the expected structural fields. It is **not** proof of route feasibility, solver feasibility, optimality, or reproducibility of a published result.

Do not add time windows, prices, charging curves, fleet heterogeneity, road gradients or other missing fields without labelling the result as a derived instance and recording every assumption.

## Citation

If you use this repository, please cite the collection **and** the original dataset release and primary paper for each benchmark family used. Copy-ready APA, IEEE, BibTeX and Chicago styles are in [docs/CITATION_AND_PROVENANCE.md](docs/CITATION_AND_PROVENANCE.md). The repository also provides [CITATION.cff](CITATION.cff).

## Licensing

The software code is MIT-licensed. Each dataset retains its own licence and attribution requirements. Public availability does not imply redistribution rights; some datasets may only be linked with download instructions. Review the README and licence of every source folder before commercial or public redistribution.

## Contributing

New datasets, format adapters, parameter dictionaries and validation tests are welcome. Follow [CONTRIBUTING.md](docs/CONTRIBUTING.md), open a dataset issue first for a new source, and submit a PR with provenance, licence review, tests and a validation report.

## Scope and roadmap

Current release: catalogue + two parser-validated snapshots + source-specific acquisition workflow + configurable CI. Next work: run the acquisition workflow once per missing source, review each PR/licence issue, add dedicated semantic parsers for each accepted format, implement a canonical typed schema and mathematical consistency checks, then introduce solver adapters and reproducible algorithm benchmarking.
