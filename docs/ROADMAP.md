# Roadmap

## Phase 1 — source-aware smoke tests (current)
- Keep supplied raw snapshots immutable.
- Parse the two supplied formats.
- Validate source registry and dataset-to-publication links.
- Produce reports and manual GitHub Actions artifacts.

## Phase 2 — controlled ingestion
- Add adapters for Montoya/VRP-REP, DIMACS E-VRP-NL-C, mixed fleet, gradient, dynamic pricing, 2E-EVRP, Felipe GVRP-MTPR and EVRPBTW-USUT.
- Download only from official/author repositories.
- Store release, DOI, commit, licence, retrieval timestamp, checksums and archive inventory.
- Keep external archives out of Git when licences or repository size require it; CI downloads pinned releases on demand.

## Phase 3 — canonical schema and provenance graph
- Define typed instance schema and parameter units.
- Add parent/child relationships for modified and generated instances.
- Add format round-trip tests and schema-version migrations.

## Phase 4 — mathematical validation
- Node/ID consistency, demand totals, distance and travel-time matrix checks.
- Battery reachability screening and charger connectivity.
- Time-window consistency and service-time checks.
- Charger-capacity/queue consistency, nonlinear charging curve monotonicity, tariff and V2G bounds.
- These checks are still not an optimization proof or solver feasibility certificate unless a full route solution is checked.

## Phase 5 — solver adapters
- Common read-only dataset interface for custom formulations, Gurobi, OR-Tools, PyVRP (where model semantics fit), ALNS, BPC, LLP and NIP.
- Never coerce unsupported features into a solver model silently.

## Phase 6 — reproducible experiments
- Multi-seed runs, time limits, hardware metadata, solver versions, objective definitions, BKS/optimality gap, feasibility and runtime.
- Produce publication-ready tables and machine-readable result bundles.
