# EM-DARP electric shuttle demand-responsive routing dataset (adjacent family)

> **Dataset ID:** `EVRP-015`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** electric mobility DARP, electric shuttle routing, demand-responsive transport  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://zenodo.org/records/23468137
- Dataset DOI: 10.5281/zenodo.23468137
- Version/snapshot: Version 1 (2026-10-19)
- Licence / redistribution: verify exact Zenodo record licence before redistribution

## 2. Description and research use cases

['electric shuttle and demand-responsive routing', 'mobility-oriented DARP research', 'adjacent electric fleet benchmarks']

Problem families: electric mobility DARP, electric shuttle routing, demand-responsive transport.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `benchmark_instances.csv` | Tabular summary of electric shuttle DARP benchmark cases; inspect column names, types and units in the release. |
| `benchmark_instances.json` | Structured representation of benchmark cases; preserve schema/version and nested request/vehicle data. |
| `benchmark_instances.tex` | Typeset benchmark summary table; useful for documentation, not a substitute for machine-readable instance data. |
| `electric shuttle routing parameters (inspect release metadata)` | Electric shuttle fleet, passenger requests, service constraints, charging and travel attributes; must be confirmed from the exact release before use. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EM-DARP": "candidate_direct (dataset files and associated paper need inspection)",
  "freight_EVPRTW": "not_applicable"
}
```

Compatibility means the source is potentially suitable based on available fields. It does not certify feasibility or guarantee that the currently implemented parser supports this format.

## 5. Local files and use

No original instance files are currently included here. This is intentional: the source is catalogued, but acquisition, archive checksum, version pinning, licence review and parser validation have not yet been completed. Do not interpret this folder as an integrated dataset.

Acquisition checklist:

1. Open the official source above and select a fixed version/release.
2. Download the original archive without renaming files.
3. Record the archive URL, download date, version and SHA-256.
4. Review the exact redistribution licence. If redistribution is not permitted or unclear, keep a download script/instructions rather than copying the raw files.
5. Extract under this folder's `instances/` subdirectory.
6. Add/extend a parser and tests; run the dataset-specific validation workflow.
7. Update `data/registry/evrp_dataset_registry.json` and `data/acquisition_status.csv` only after successful validation.

Suggested command after the dataset adapter is implemented:

```bash
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw --out reports --dataset EVRP-015
```

## 6. Primary citations

No verified primary citation linked yet; open an issue before using this record in a paper.

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
