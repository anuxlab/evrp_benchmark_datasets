# Contributing to EVRP Benchmark Datasets

Thank you for helping expand the EVRP benchmark collection. Contributions may add a dataset source, raw instance files (when redistribution is permitted), parser support, metadata, tests, compatibility rules or documentation.

## 1. Before adding a dataset

Open a **Dataset source proposal** issue using the `dataset-source.yml` template. Include:

- Official dataset landing page and exact release/version
- Dataset DOI and primary paper DOI
- Problem family and mathematical features
- Expected instance count and file formats
- Parameter names, definitions and units
- Licence / redistribution permissions
- Best-known solutions or benchmark results, if available
- Known parent dataset and transformations, if derived

Do not upload files with unclear licensing. A public download link is not a redistribution licence.

## 2. Required folder layout

Create one folder under `data/raw/<dataset-short-name>/`:

```text
data/raw/<dataset-short-name>/
├── README.md
├── dataset.json
├── LICENSE.txt                 # if supplied/permitted by source
├── instances/                  # original files, if redistribution is permitted
└── checksums.sha256
```

The folder README must explain:

1. Source, version, DOI and primary paper
2. Dataset purpose and problem family
3. Expected file count and exact file list
4. Every parameter, original symbol, normalized name, unit and definition
5. Instance naming conventions and family structure
6. Which EVRP variants are direct/conditional/unsupported and why
7. Download/use instructions
8. Licence and citation requirements
9. Validation command and known limitations

If raw files cannot be redistributed, keep `instances/` absent and provide a reproducible download script or exact source instructions. Mark the dataset as `catalogued_not_yet_ingested`.

## 3. Registry and provenance

Update `data/registry/evrp_dataset_registry.json` and `data/acquisition_status.csv`. Required information:

- Unique `dataset_id`
- Official URL and pinned release/commit/DOI
- Publication and dataset citation IDs
- Expected and observed instance counts
- Licence status and redistribution decision
- Parameter inventory and problem-family compatibility
- Repository folder and local integration status

Do not claim `locally_ingested_and_parser_validated` until the raw files are present, checksums are recorded, parser tests pass and the report artifact is generated.

## 4. Parser and tests

- Add a dedicated parser or extend an existing parser without changing the source files.
- Add at least one small fixture and tests for normal, malformed and boundary cases.
- Test missing values, duplicate node IDs, invalid capacities, invalid time windows and inconsistent dimensions where relevant.
- Preserve source units and symbols. Never silently infer units.
- Add explicit `source`, `derived`, `assumed` or `missing` provenance labels for each normalized parameter.
- Add compatibility tests for every problem variant claimed by the source.

## 5. Run checks locally

```bash
python -m pip install -e ".[test]"
PYTHONPATH=src pytest -vv
PYTHONPATH=src python -c "from pathlib import Path; from evrp_bench.registry import load_registry, validate_registry; e=validate_registry(load_registry(Path('data/registry/evrp_dataset_registry.json'))); print(e or 'Registry OK'); raise SystemExit(bool(e))"
PYTHONPATH=src python -m evrp_bench.runner --data data/raw --out reports --dataset <DATASET-ID>
```

Attach `dataset_report.json`, `dataset_summary.csv`, `dataset_report.md`, and the console log to the PR when adding parser support.

## 6. Pull request process

1. Fork the repository and create a focused branch, e.g. `data/add-evrpnl-source`.
2. Make a small, reviewable change. Keep raw snapshots immutable.
3. Update dataset README, registry, citations, acquisition status, checksums and tests.
4. Run all local checks.
5. Open a PR using the repository template and link the dataset proposal issue.
6. Wait for `PR validation` checks. Resolve failures and request review.
7. Do not mark an external source as integrated until all checks pass and maintainers confirm the licence/provenance.

## 7. What CI checks

Pull-request Actions validate registry schema, unique dataset IDs, required source/citation links, dataset-folder READMEs, local file inventory, parser tests and generated report consistency. Manual workflows provide full/filtered corpus runs. A parser pass is not a mathematical feasibility or optimality certificate.

## 8. Issue labels

Use `datasets` for source/data problems, `parser` for format bugs, `documentation` for docs, `citations` for attribution, `ci-failure` for Actions failures and `workflow-failure` for automated run failures.
