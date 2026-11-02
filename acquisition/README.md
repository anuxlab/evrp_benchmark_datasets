# Dataset acquisition adapters

This directory contains source-specific acquisition policy and adapter configuration for the 13 catalogue entries that do not yet have local raw files.

## One collection per workflow run

Run **Actions → Dataset acquisition → Run workflow** and select exactly one `EVRP-003` … `EVRP-015`. This is intentional: it makes each source's version, download, legal gate, validation output, and any issue independently auditable.

The runner uses these adapters:

| Adapter | Collections | Retrieval method |
|---|---|---|
| VRP-REP | EVRP-003, EVRP-006 | Discover and retrieve official dataset links from the dataset record |
| DIMACS derived | EVRP-004 | Retrieve the Montoya base set and record the two charger-capacity derivations; no fabricated variants |
| Mendeley Data | EVRP-005, EVRP-008, EVRP-009, EVRP-010, EVRP-012 | Public dataset/file API; optional `MENDELEY_ACCESS_TOKEN` secret if the host requires authenticated API access |
| Zenodo | EVRP-007, EVRP-015 | Zenodo Records API; download the source archive and relevant metadata |
| Dryad | EVRP-011 | Dryad REST API v2; resolve the published version and file downloads |
| GitHub | EVRP-013, EVRP-014 | GitHub API; pin the resolved commit and download its source archive |

## Redistribution gate

The workflow downloads to the ephemeral runner first. It does **not** equate public availability with permission to redistribute.

Current policy configuration in `sources.json`:

- **Automatic PR candidates:** EVRP-005, EVRP-008, EVRP-009, EVRP-010, EVRP-012 (Mendeley CC BY 4.0) and EVRP-014 (upstream CC0-1.0).
- **Manual rights review; never auto-committed:** EVRP-003, EVRP-004, EVRP-006 (VRP-REP/DIMACS terms), EVRP-007 and EVRP-015 (Zenodo record-level licence confirmation required), EVRP-011 (Dryad version/file rights), EVRP-013 (no repository licence file identified).

The source-specific evidence URL and rationale are included in every source entry. A maintainer must verify the actual current record/version before changing a manual-review source to `verified`. Do not change the flag merely to make a workflow pass.

## Validation and repository updates

The acquisition script:

1. resolves a pinned source version or commit;
2. downloads into `acquisition-staging/<dataset-id>/`;
3. checks archive integrity and safe extraction paths (path traversal and symlink entries are rejected);
4. validates non-empty data files, JSON syntax and XLSX container integrity;
5. computes SHA-256 for each data file;
6. records source metadata, version, licence evidence and file inventory.

For sources whose instance count cannot be inferred safely from file names, the count remains unknown until a domain-specific parser is implemented. Workbooks/configuration collections are not counted as one instance per file.

If the licence gate passes and structural validation succeeds, the runner copies the files into the dataset's `data/raw/` folder, updates registry/acquisition metadata, and creates a **pull request**, never a direct push to `main`. The README's integrated-collection count is refreshed at that point. The parser-validated instance badge remains unchanged until a dataset-specific parser passes.

If acquisition or validation fails, an issue is opened with `datasets`, `dataset-acquisition`, `acquisition-failure`, and `needs-maintainer`. If the download succeeds but redistribution is not verified, an issue is opened with `licensing-review` and `needs-maintainer`; files remain only in the runner artifact and are not committed.

## Optional secrets

- `MENDELEY_ACCESS_TOKEN`: OAuth access token for Mendeley Data API requests. The Mendeley API documents OAuth2 authentication; configure this repository secret before dispatching Mendeley-backed collections. If the token is absent/expired or the API denies access, the workflow opens an acquisition-failure issue with the API response rather than attempting an unofficial mirror.
- `GITHUB_TOKEN`: automatically supplied by GitHub Actions for public GitHub API access and issue operations.
- `GH_PR_TOKEN`: optional fine-grained token with `contents: write` and `pull-requests: write`. If supplied, it lets the generated PR trigger the repository's normal `pull_request` checks. Without it, the acquisition workflow runs the repository test suite before opening the PR, but GitHub's `GITHUB_TOKEN` event-suppression rules may prevent the PR from triggering other workflows.

In **Settings → Actions → General → Workflow permissions**, grant the workflow read/write access for contents and pull requests, and enable **Allow GitHub Actions to create and approve pull requests**. GitHub documents that this separate setting is required for automated PR creation.

Do not add credentials to `sources.json` or commit them.

## Current limitations

- Generic structural validation is not a semantic benchmark parser, a feasibility checker, or an optimality certificate.
- EVRP-004 is a derived family: the 240 cases are two charger-capacity variants of 120 Montoya base instances. The workflow does not claim to have acquired 240 separate original files.
- EVRP-012 includes workbooks whose sheets need a dataset-specific parser before instance counts can be published.
- EVRP-013 and EVRP-014 are adjacent electric-mobility families, not standard freight EVRP datasets.
- Mendeley and some repository APIs may change or require credentials; failures are reported as issues rather than silently substituting third-party mirrors.
