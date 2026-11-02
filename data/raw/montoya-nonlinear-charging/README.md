# Montoya et al. nonlinear charging benchmark

> **Dataset ID:** `EVRP-003`  
> **Published/expected instance count:** 120  
> **Problem family:** E-VRP-NL  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://www.vrp-rep.org/datasets/item/2016-0020.html
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: VRP-REP ID 2016-0020
- Licence / redistribution: VRP-REP public listing; instance-level redistribution terms require source check

## 2. Description and research use cases

nonlinear charging; partial recharge; comparison of charging models; charging-decision heuristics

Problem families: E-VRP-NL.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `customer service times` | Duration of service at a customer; distinguish service duration from charging and waiting time. |
| `charging stations` | Facility nodes at which energy replenishment is possible; inspect station attributes and availability. |
| `battery capacity` | Maximum usable onboard energy / state-of-charge capacity; retain source energy units and initial SOC assumptions. |
| `travel times` | Arc travel durations or travel-time matrix; retain time unit and any time dependence. |
| `arc energy consumption` | Energy consumed on each travel arc; record whether load, grade, speed and regeneration are included. |
| `piecewise-linear concave charging curves` | Charging time or energy accumulation represented by piecewise segments; preserve breakpoints, slopes and units. |
| `partial recharge decisions` | Decision variable for how much energy to add at a charging stop; not equivalent to mandatory full recharge. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "E-VRP-NL": "direct_fit",
  "linear_charging_EVRP": "conditional_fit (model simplification)",
  "E-VRPTW": "unsupported unless windows supplied"
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
  --data data/raw --out reports --dataset EVRP-003
```

## 6. Primary citations

- Alejandro Montoya, Christelle Guéret, Jorge E. Mendoza, Juan G. Villegas (2017). *The electric vehicle routing problem with nonlinear charging function*. Transportation Research Part B: Methodological, 103, 87–110. https://doi.org/10.1016/j.trb.2017.02.004

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-003`. The source-specific adapter is `vrp_rep`.

- Source/version: [VRP-REP ID 2016-0020](https://www.vrp-rep.org/datasets/item/2016-0020.html)
- Current redistribution gate: **manual_review**
- Automatic repository inclusion: **disabled pending explicit maintainer rights review**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
