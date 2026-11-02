# Changelog

## 0.4.0 — 2026-11-02

- Added a manually triggered, one-dataset-per-run acquisition workflow for EVRP-003 through EVRP-015.
- Added source-specific adapters for VRP-REP, DIMACS-derived variants, Mendeley Data, Zenodo, Dryad and GitHub.
- Added archive path-traversal/symlink checks, expansion/download limits, archive integrity checks, CSV/JSON/XLSX structural checks and SHA-256 inventories.
- Added a redistribution gate: only explicitly configured CC BY 4.0/CC0 sources can create a pull request; unclear/restricted sources remain runner artifacts and open licensing-review issues.
- Added automatic PR creation for successful licence-cleared acquisitions; failure and legal-review issues carry source, version, validation and run details.
- Added registry, acquisition-status CSV, manifest and README count updates after successful acquisition validation only.
- Separated raw acquisition/schema validation from semantic parser validation; the existing EVRP-001/002 parser corpus remains isolated until additional parsers are implemented.
- Preserved the latest supplied successful validation and smoke-test reports/logs.
- Local verification: 18 tests passed; all four workflow YAML files parsed; Python sources compile.

## 0.3.0 — 2026-11-02

- Expanded the dataset source catalogue to 15 source collections.
- Added a source-specific README and `dataset.json` card to every dataset folder.
- Explicitly separated catalogue records from locally integrated raw datasets.
- Added an acquisition-status matrix and SHA-256 manifest for local raw files.
- Added copy-ready APA 7, IEEE, BibTeX and Chicago repository citations.
- Added root contribution guidelines, issue forms and pull-request template.
- Added configurable manual GitHub Actions workflow with dataset, problem-family, instance-mode, exact-filename and validation-depth inputs.
- Added automated labelled issue creation for workflow failures.
- Added pull-request validation checks.
- Preserved the supplied GitHub Actions runner logs and original JSON/CSV/Markdown report export.
- Added local retest logs and regenerated full-corpus reports.
- Updated workflow actions to Node 24-compatible major versions to address the deprecation warning in the supplied runner export.
- Local verification: 13 tests passed; 109/109 local instances passed parser-level validation.

## 0.2.0

- Added source registry, problem taxonomy, citation/provenance documentation and expanded source catalogue.
- Added local parsers for Mavrovouniotis EVRP and Schneider/Goeke EVRPTW files.

## 0.1.0

- Initial uploaded benchmark snapshots and parser smoke tests.

## [0.3.1] - 2026-11-02

### Fixed
- Move checkout before creating `reports/` and `runner-logs/`; `actions/checkout` cleans the workspace and had removed the directories created earlier, causing `tee` to exit with `No such file or directory` in both validation workflows.
- Pass custom workflow selections to the failure-issue step using GitHub Actions expressions (`${{ inputs.* }}`) rather than literal JavaScript template fragments, so issue metadata records the actual inputs.

### Verified locally
- Python test suite: 13 passed.
- All three workflow YAML files parse successfully.
