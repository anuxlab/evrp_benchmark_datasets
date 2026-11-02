# Akbay et al. expanded two-echelon EVRP dataset

> **Dataset ID:** `EVRP-007`  
> **Published/expected instance count:** 3000  
> **Problem family:** 2E-EVRP, 2E-EVRPTW, SPD, partial delivery  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://zenodo.org/records/14844216
- Dataset DOI: 10.5281/zenodo.14844216
- Version/snapshot: Version 2 (2025)
- Licence / redistribution: Zenodo record describes software/data release; verify archive-level licence before republishing

## 2. Description and research use cases

two-echelon logistics; satellites; time windows; simultaneous pickup/delivery; partial deliveries; scale tests

Problem families: 2E-EVRP, 2E-EVRPTW, SPD, partial delivery.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `central depot` | Origin facility feeding first-echelon routes or satellites. |
| `satellite depots` | Intermediate facilities where freight is transferred between vehicle echelons. |
| `two vehicle echelons` | Separate routing stages, typically depot-to-satellite and satellite-to-customer, with distinct fleet/flow constraints. |
| `customer coordinates and demand` | Location and required quantity of each customer. |
| `time windows` | Permitted service-start or service interval at a customer; verify the exact semantics of earliest/latest service. |
| `EV battery and load capacities` | Energy and payload limits; check whether limits differ by echelon or vehicle class. |
| `SPD and partial delivery flags` | Source-specific flags for split deliveries and partial delivery; verify the exact definition in the dataset paper. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "2E-EVRP": "direct_fit",
  "2E-EVRPTW": "direct_fit",
  "single_echelon_EVRP": "unsupported without documented projection"
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
  --data data/raw --out reports --dataset EVRP-007
```

## 6. Primary citations

- Mehmet Anıl Akbay, Çağrı B. Kalaycı, Christian Blum, Oya Polat (2022). *Variable neighborhood search for the two-echelon electric vehicle routing problem with time windows*. Applied Sciences, 12(3), 1014. https://doi.org/10.3390/app12031014
- Mehmet Anıl Akbay, Christian Blum (2025). *A dataset for two-echelon electric vehicle routing problems*. Data in Brief, 60, 111470. https://doi.org/10.1016/j.dib.2025.111470

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-007`. The source-specific adapter is `zenodo`.

- Source/version: [v2](https://zenodo.org/records/14844216)
- Current redistribution gate: **manual_review**
- Automatic repository inclusion: **disabled pending explicit maintainer rights review**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
