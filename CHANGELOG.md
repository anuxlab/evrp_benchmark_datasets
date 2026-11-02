# Changelog

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
