# Runner logs and validation artifacts

## Supplied GitHub Actions run snapshot

This repository snapshot includes the full runner log export supplied for GitHub Actions run **41391970434**:

- Run URL: https://github.com/anuxlab/evrp_benchmark_datasets/actions/runs/41391970434
- Commit checked out: `b5214315c66ce208be43da2b096684128e5a0a0e`
- Runner: Ubuntu 26.04 hosted runner
- Python: 3.11.17
- Workflow job: `validate`
- Files discovered / available: 109 / 109
- Parser-level passes / failures: 109 / 0
- Formats: 17 `mavrovouniotis_evrp`, 92 `schneider_evrptw_tabular`
- Registry validation: passed
- Artifact ID: `13117487481`

The raw log text files are preserved under `artifacts/runner_logs/run-41391970434/`, including the full `0_validate.txt` and individual step logs. The JSON/CSV/Markdown inspection report and registry snapshot supplied from that same run are preserved under `artifacts/runner_reports/run-41391970434/`.

## Important log interpretation

The run succeeded. It produced Node.js deprecation warnings for older action versions forced to Node 24; these were warnings, not job failures. The run did not acquire the other 13 catalogued source families. It only inspected the 109 files already present in `data/raw`.

## Future workflow artifacts

Each custom or smoke workflow run uploads:

- Runner context and environment
- Dependency installation log
- Pytest output
- Registry validation output
- Per-instance parser output
- JSON report, CSV summary and Markdown report
- Run metadata and selected workflow inputs

Artifacts are retained for 90 days in the custom workflow. The full GitHub Actions web log remains accessible from the run URL while GitHub retains the run.

## Automated failure issues

On a failed workflow, Actions creates an issue labelled `datasets`, `ci-failure`, and `workflow-failure`, with the run URL, commit and selected dataset/variant. Download the attached artifact before diagnosing the issue. Do not close the issue until the cause is fixed and a successful rerun is linked.

## Local artifact retest (release 0.3.0)

The reproducibility checks executed while assembling this release are stored under `artifacts/local_validation/2026-11-02/`:

- `pytest.log`: full unit test output (13 passed).
- `full_corpus.log`: all 109 locally available instances (109 passed).
- `dataset_evrp001.log`: dataset-ID selection test (17 passed).
- `custom_instance.log`: exact filename selection test (1 passed).

The current generated machine-readable corpus report is under `reports/`.


## Latest supplied successful runs (2 November 2026)

The following user-supplied exports are preserved under `artifacts/latest_successful_runs/`:

- Run `41397493333`: custom validation, standard level, all datasets/variants, 109 parser passes.
- Run `41397615476`: custom validation, strict level, all datasets/variants, 109 parser passes.
- Latest smoke export: 13 tests passed, registry passed, 109 locally parser-supported files passed.

These exports confirm the existing two parser-enabled corpora. They do not mean that the 13 remaining catalogued sources were downloaded.
