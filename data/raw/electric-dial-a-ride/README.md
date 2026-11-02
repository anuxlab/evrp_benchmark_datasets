# Electric autonomous dial-a-ride benchmark (adjacent family)

> **Dataset ID:** `EVRP-013`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** eADARP, electric dial-a-ride, ride-pooling  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://github.com/claudiabongiovanni/eADARP
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: GitHub repository snapshot; pin commit
- Licence / redistribution: repository licence/file terms should be checked

## 2. Description and research use cases

on-demand mobility; passenger routing; ride-pooling; battery-constrained DARP

Problem families: eADARP, electric dial-a-ride, ride-pooling.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `requests/origins/destinations` | Passenger demand represented by pickup and drop-off locations, not freight customer nodes. |
| `time windows and ride-time constraints` | Pickup/drop-off availability windows and passenger maximum ride-time constraints. |
| `depots` | Vehicle start/end facilities; record whether multiple depots are allowed. |
| `charging stations` | Facility nodes at which energy replenishment is possible; inspect station attributes and availability. |
| `vehicle capacities` | Passenger or load capacity; do not equate passenger capacity with freight payload. |
| `initial battery inventory` | Initial state-of-charge / energy for each vehicle or fleet. |
| `recharge rates` | Energy replenishment rate or charging curve; station-specific if supplied. |
| `Uber-derived travel times` | Travel-time matrix estimated from ride-hailing trip data; check aggregation, time period and privacy/licence conditions. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "eADARP": "direct_fit",
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
  --data data/raw --out reports --dataset EVRP-013
```

## 6. Primary citations

- Claudia Bongiovanni, Moshe Kaspi, Nikolas Geroliminis (2019). *The electric autonomous dial-a-ride problem*. Transportation Research Part B: Methodological, 122, 436–456. https://github.com/claudiabongiovanni/eADARP
- Tai-Yu Ma, Yumeng Fang (2022). *Survey of charging management and infrastructure planning for electrified demand-responsive transport systems: Methodologies and recent developments*. European Transport Research Review, 14, article 36. https://doi.org/10.1186/s12544-022-00560-3

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
