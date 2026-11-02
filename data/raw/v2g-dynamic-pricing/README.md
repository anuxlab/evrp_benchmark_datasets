# V2G and dynamic energy pricing extended EVRPTW

> **Dataset ID:** `EVRP-008`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** EVRPTW-V2G, time-of-use energy pricing  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://data.mendeley.com/datasets/dmnhggw478/1
- Dataset DOI: 10.17632/dmnhggw478.1
- Version/snapshot: Version 1 (2026)
- Licence / redistribution: CC BY 4.0

## 2. Description and research use cases

energy-cost optimization; V2G revenue; time-dependent charging; grid interaction

Problem families: EVRPTW-V2G, time-of-use energy pricing.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `base EVRPTW data` | Parent time-window electric routing fields; cite and preserve the exact parent release. |
| `vehicle-to-grid capability` | Ability to export stored battery energy to the grid, with power, efficiency and state-of-charge bounds. |
| `time-of-use energy tariffs` | Electricity price indexed by time and potentially station; preserve currency, energy unit and time zone. |
| `time-dependent charge/discharge decisions` | Charging and grid-export choices that depend on time, SOC and tariff; requires temporal discretization or continuous-time policy. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EVRPTW-V2G-DP": "candidate_direct (schema validation pending)",
  "static_EVPR": "conditional_fit"
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
  --data data/raw --out reports --dataset EVRP-008
```

## 6. Primary citations

- Luis Fernando Rodriguez Jimenez (2026). *Extended Benchmark Instances for the Electric Vehicle Routing Problem with V2G and Dynamic Energy Pricing*. Mendeley Data, Version 1. https://doi.org/10.17632/dmnhggw478.1

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
