# Felipe et al. GVRP multiple technologies and partial recharges

> **Dataset ID:** `EVRP-006`  
> **Published/expected instance count:** 41  
> **Problem family:** GVRP-MTPR, multiple charging technologies, partial recharge  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://www.vrp-rep.org/datasets/item/2018-0004.html
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: VRP-REP ID 2018-0004
- Licence / redistribution: VRP-REP public listing; source terms to be checked

## 2. Description and research use cases

partial recharge; charger technology choice; mixed charging infrastructure

Problem families: GVRP-MTPR, multiple charging technologies, partial recharge.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `multiple recharge technologies` | Different charging or refuelling technologies available to vehicles; identify which vehicle can use each technology. |
| `station/technology compatibility` | Compatibility relation between vehicle type and station technology. |
| `partial recharge amounts` | Energy quantity selected at each charging event; may interact with station technology and charging duration. |
| `vehicle autonomy` | Maximum travel range or energy availability under a specified load/operating condition. |
| `geographical instance attributes` | Node coordinates, spatial distribution and/or network geometry used to define instance layout. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "GVRP-MTPR": "direct_fit",
  "single_technology_EVRP": "conditional_fit (restrict technology choices)"
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
  --data data/raw --out reports --dataset EVRP-006
```

## 6. Primary citations

- Ángel Felipe, M. Teresa Ortuño, Giovanni Righini, Gregorio Tirado (2014). *A heuristic approach for the green vehicle routing problem with multiple technologies and partial recharges*. Transportation Research Part E: Logistics and Transportation Review, 71, 111–128. https://doi.org/10.1016/j.tre.2014.09.003

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
