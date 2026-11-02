# Roadmap and integration status

## Current release — 0.3.0

- 15 curated source folders with dataset-specific README and `dataset.json` cards.
- 2 locally ingested datasets and 109 locally parser-validated instances.
- Registry, acquisition-status matrix, checksums and citation graph.
- Configurable manual GitHub Actions workflow with dataset, problem-family and instance selectors.
- Separate smoke workflow and pull-request validation.
- Failure-to-Issue automation and complete supplied runner-log/report snapshot.

## Phase 1 — completed: source-aware smoke tests

- Preserve the 17-file Mavrovouniotis upload and 92-file Schneider/Goeke Mendeley snapshot.
- Parse the two local formats.
- Validate registry and dataset provenance.
- Produce JSON, CSV and Markdown reports.

## Phase 2 — in progress: controlled acquisition of remaining sources

Acquire each of the 13 currently catalogued but non-ingested sources from its official host. For each release:

1. Confirm exact version, DOI or commit.
2. Review redistribution licence and commercial restrictions.
3. Download original archive or prepare reproducible download instructions.
4. Record archive checksum, file inventory and retrieval timestamp.
5. Add a format adapter and dataset-specific test fixtures.
6. Update local integration status only after parser and provenance tests pass.

Priority order:
1. Montoya EVRP-NL and Froger/DIMACS EVRP-NL-C.
2. Goeke-Schneider mixed fleet and Felipe multiple technologies/partial recharge.
3. Akbay two-echelon EVRP.
4. V2G/dynamic pricing and gradient-aware EVRPTW.
5. Remaining uncertainty, LEZ and adjacent electric mobility collections.

## Phase 3 — canonical schema and provenance graph

- Define typed instance schema and explicit units.
- Track parent/child relationships for modified and generated instances.
- Add parser versioning and schema migrations.
- Retain source-specific fields that cannot yet be normalized.

## Phase 4 — mathematical consistency validation

- Node/ID consistency, demand totals, distance and travel-time matrix checks.
- Battery reachability screening and charging-station connectivity.
- Time-window and service-time consistency.
- Charger-capacity/queue consistency, nonlinear charging curve monotonicity, tariff and V2G bounds.
- Explicit assumptions for every derived field.

## Phase 5 — solver adapters

- Common read-only dataset interface for custom formulations, Gurobi, OR-Tools, PyVRP (only where model semantics fit), ALNS, BPC, LLP and NIP.
- Never coerce unsupported features into a solver model silently.

## Phase 6 — reproducible experiments

- Multi-seed runs, time limits, hardware metadata, solver versions and objective definitions.
- BKS/optimality gap, feasibility and runtime reporting.
- Publication-ready tables and machine-readable experiment bundles.

## Release criteria

A source collection is counted as locally integrated only when raw files are present or reproducibly fetched, licence reviewed, checksums stored, parser support implemented, test fixtures passing, and per-instance validation artifacts published.
