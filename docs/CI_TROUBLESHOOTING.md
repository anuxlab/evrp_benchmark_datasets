# CI failure triage — 2 November 2026

## Root cause of the two automatically opened issues

Both failures occurred before the parser or dataset checks ran. The workflows created `reports/` and `runner-logs/`, then ran `actions/checkout`. Checkout cleans the workspace, removing those newly created directories. The next command piped output through `tee runner-logs/...`, and `tee` failed with `No such file or directory` (exit code 1).

The fix is to run checkout first and create output directories immediately afterwards. This has been applied to:

- `.github/workflows/dataset-smoke-tests.yml`
- `.github/workflows/custom-benchmark-validation.yml`

The custom-validation failure handler also previously declared environment values as literal strings such as `${process.env.INPUT_DATASET}`. These have been replaced with GitHub Actions input expressions so the issue body receives the selected dataset, problem family, instance mode and validation level.

## What the uploaded reports establish

The 2 November full-corpus report records 109 locally available files validated: 17 Mavrovouniotis EVRP instances and 92 Schneider/Goeke EVRPTW instances. It also explicitly lists EVRP-003 through EVRP-015 as having no local raw files. Thus, 109 passed means all 109 files currently present passed; it does not mean all 15 catalogued collections are locally integrated.

## Closure policy

Do not close the two CI issues merely because the Python report shows 109 passed. The reported CI runs failed at log setup and did not reach the test/runner steps. After merging the workflow fix:

1. Manually run **EVRP dataset smoke tests** with `run_full_corpus=true`.
2. Manually run **Custom EVRP benchmark validation** with `dataset=EVRP-001`, `problem_variant=EVRP`, `instance_mode=all`, `validation_level=strict`, and `fail_on_empty=true`.
3. Confirm both jobs are green, artifacts contain `runner-logs/01-install.txt`, pytest logs, registry logs, runner logs and reports, and the custom failure issue metadata is correctly populated if you test the failure path.
4. Close #1 and #2 as fixed-by-commit, linking the successful runs. If either new run fails, keep the corresponding issue open and diagnose the new error rather than closing it.

## Dataset acquisition policy

The current smoke and custom-validation workflows validate files already committed under `data/raw/`. They do not download external collections and do not commit files back to the repository. Automated acquisition should be a separate manually triggered workflow with source-specific adapters, licence/redistribution checks, archive checksum verification, parser validation and a protected commit step. Never commit a dataset merely because a runner can download it: only commit when the source licence explicitly permits redistribution. Otherwise validate in the runner workspace, retain permitted metadata/reports, and point users to the authoritative source.
