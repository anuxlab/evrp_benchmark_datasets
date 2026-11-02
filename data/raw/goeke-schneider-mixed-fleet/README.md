# Goeke-Schneider mixed-fleet EVRPTW-MF

> **Dataset ID:** `EVRP-005`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** EVRPTW-MF, mixed electric/ICE fleet  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://data.mendeley.com/datasets/bd7rm5fw6k/1
- Dataset DOI: 10.17632/bd7rm5fw6k.1
- Version/snapshot: Version 1 (2022)
- Licence / redistribution: CC BY 4.0

## 2. Description and research use cases

mixed powertrain fleet; fleet allocation; real-world energy model; mixed-fleet routing

Problem families: EVRPTW-MF, mixed electric/ICE fleet.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `EV and conventional vehicle fleet types` | Fleet contains battery-electric and internal-combustion vehicle types with different feasibility, cost and emissions parameters. |
| `time windows` | Permitted service-start or service interval at a customer; verify the exact semantics of earliest/latest service. |
| `speed` | Vehicle speed or speed profile used to convert distance to travel time; identify per-vehicle or time-dependent definitions. |
| `road gradient` | Road slope/elevation change affecting traction energy and potentially regenerative energy. |
| `cargo-load distribution` | Vehicle payload along the route; may change arc energy use and vehicle feasibility. |
| `energy consumption` | Energy required to traverse an arc; determine whether it depends on distance, speed, vehicle load, road grade or vehicle type. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EVRPTW-MF": "direct_fit",
  "homogeneous_EV": "conditional_fit (restrict fleet to EVs)",
  "ICE-EVRP": "direct_fit"
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
  --data data/raw --out reports --dataset EVRP-005
```

## 6. Primary citations

- Dominik Goeke, Michael Schneider (2015). *Routing a mixed fleet of electric and conventional vehicles*. European Journal of Operational Research, 245(1), 81–99. https://doi.org/10.1016/j.ejor.2015.01.049
- Dominik Goeke, Michael Schneider (2022). *EVRPTW-MF*. Mendeley Data, Version 1. https://doi.org/10.17632/bd7rm5fw6k.1

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-005`. The source-specific adapter is `mendeley`.

- Source/version: [1](https://data.mendeley.com/datasets/bd7rm5fw6k/1)
- Current redistribution gate: **verified**
- Automatic repository inclusion: **eligible after the runner re-verifies the source metadata and validation**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
