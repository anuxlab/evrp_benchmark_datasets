# Initial corpus validation snapshot

**Source run:** [GitHub Actions run 41391970434](https://github.com/anuxlab/evrp_benchmark_datasets/actions/runs/41391970434)  
**Commit:** `b5214315c66ce208be43da2b096684128e5a0a0e`  
**Runner:** Ubuntu 26.04, Python 3.11.17  
**Run date:** 2 November 2026

| Metric | Result |
|---|---:|
| Files discovered | 109 |
| Files available | 109 |
| Parser-level passes | 109 |
| Parser-level failures | 0 |
| Mavrovouniotis EVRP format | 17 |
| Schneider EVRPTW tabular format | 92 |
| Registry validation | Passed |

The full runner logs and report files supplied for this run are preserved under `artifacts/runner_logs/run-41391970434/` and `artifacts/runner_reports/run-41391970434/`.

**Scope limitation:** this run validated only the two raw collections present at that commit. It did not download or validate the other 13 catalogued source families. A parser pass is not a mathematical feasibility, route feasibility or optimality certificate.

## Local Phase 0.3.0 artifact retest

- Unit tests: **13 passed**.
- Full local corpus rerun: **109 discovered, 109 passed, 0 failed**.
- Dataset selector: EVRP-001 returned 17 instances.
- Problem selector: EVRP-001 + E-CVRP returned 17 instances.
- Exact custom instance selector: `E-n22-k4.evrp` returned 1 instance.
- Dataset folders: 15 README files and 15 machine-readable `dataset.json` cards.
- The 13 unacquired sources are reported separately in runner metadata rather than counted as local test cases.

This release still performs structural parser validation only. The mathematical validation and optimization phases remain future work.
