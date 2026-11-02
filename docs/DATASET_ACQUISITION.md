# Dataset acquisition and redistribution policy

## Objective

Acquire the 13 currently missing source collections through reproducible, source-specific adapters. Each collection is dispatched separately so its provenance and legal status can be reviewed independently.

## Acquisition state machine

```text
catalogued
   |
   v
manual workflow dispatch (one dataset)
   |
   v
official-source download to runner staging
   |
   v
archive safety + file integrity + SHA-256
   |
   +---- failed ----> upload logs + labelled acquisition issue
   |
   v
redistribution rights gate
   |
   +---- unclear/restricted ----> artifact only + licensing-review issue
   |
   v
copy raw files + update acquisition metadata
   |
   v
open pull request (never push directly to main)
   |
   v
maintainer review and merge
   |
   v
dataset-specific parser + semantic validation
   |
   v
parser-validated instance counts and benchmark use
```

## Legal decision rules

1. A public URL, repository visibility, DOI, or ability to download is not a redistribution licence.
2. Commit data only when the source record/version explicitly grants a suitable redistribution right (currently configured for CC BY 4.0 and CC0-1.0 sources).
3. Keep NC (non-commercial), unclear, missing, or conflicting terms out of `data/raw/` unless a maintainer verifies a separate permission.
4. Preserve the exact source version, DOI/commit, attribution, licence notice and source file checksums.
5. Derived datasets must retain parent provenance. A derived dataset is not an unrelated corpus.
6. Where source terms allow research use but not redistribution, keep the official source URL and acquisition instructions in the dataset README; do not commit the data.

## Counts and labels

- **Catalogued collection:** metadata and a source record exist.
- **Acquired and schema validated:** actual files were downloaded, integrity-checked and structurally inspected; no domain parser claim is made.
- **Parser validated:** a dataset-specific parser successfully parsed the instances.
- **Instance count:** update only when a source-specific rule or parser can reliably identify instances. Do not use the number of downloaded archives/workbooks as the number of benchmark instances.

The README's integrated-collection count changes only after a successful, licence-cleared acquisition. The parser-validated instance count remains unchanged until parser-level validation is complete.

## Issues and pull requests

- Download or validation failure: `datasets`, `dataset-acquisition`, `acquisition-failure`, `needs-maintainer`.
- Successful download but unclear redistribution terms: `datasets`, `dataset-acquisition`, `licensing-review`, `needs-maintainer`.
- Licence-cleared successful acquisition: open a PR tagged `datasets`, `dataset-acquisition`, `licence-reviewed`.

A PR must contain the raw files, a source archive where appropriate, SHA-256 inventory, version/commit metadata, updated registry and status CSV, and README count changes. Maintainers should review the licence evidence and file inventory before merging.
