# Gradient-aware EVRPTW with altitude information

> **Dataset ID:** `EVRP-009`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** EVRPTW-GR, gradient/load-dependent energy, regenerative braking  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://data.mendeley.com/datasets/srfdbp2twv/1
- Dataset DOI: 10.17632/srfdbp2twv.1
- Version/snapshot: Version 1 (2025)
- Licence / redistribution: CC BY 4.0

## 2. Description and research use cases

grade-aware energy use; downhill regeneration; realistic energy modelling

Problem families: EVRPTW-GR, gradient/load-dependent energy, regenerative braking.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `Schneider base instance fields` | Inherited EVRPTW nodes, demand, time windows, battery and charging parameters; record parent instance ID. |
| `altitude/elevation` | Elevation at nodes or along arcs; use source units and reference datum. |
| `road gradient` | Road slope/elevation change affecting traction energy and potentially regenerative energy. |
| `regenerative braking` | Energy recovered during deceleration/downhill travel; record efficiency and bounds rather than assuming all potential energy is recovered. |
| `load dynamics` | Change in vehicle payload along a route, affecting traction energy consumption. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EVRPTW-GR": "candidate_direct (schema validation pending)",
  "base_EVPRTW": "conditional_fit"
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
  --data data/raw --out reports --dataset EVRP-009
```

## 6. Primary citations

- Michael Schneider, Andreas Stenger, Dominik Goeke (2014). *The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations*. Transportation Science, 48(4), 500–520. https://doi.org/10.1287/trsc.2013.0490
- Sina Rastani, Merve Keskin, Tugce Yuksel, Bülent Çatay (2025). *Uphill Struggles, Downhill Gains: How Road Gradients and Load Dynamics Influence Electric Vehicle Routing Decisions?*. European Journal of Operational Research (dataset record describes article as to appear). https://data.mendeley.com/datasets/srfdbp2twv/1

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
