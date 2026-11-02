# Mixed-fleet VRP with low-emission zones (EVRPTW-derived + Milan case)

> **Dataset ID:** `EVRP-012`  
> **Published/expected instance count:** Not recorded  
> **Problem family:** mixed-fleet EVRP, low-emission-zone routing, real-road case study  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://data.mendeley.com/datasets/np452gmj7f/2
- Dataset DOI: 10.17632/np452gmj7f.2
- Version/snapshot: Version 2 (2025)
- Licence / redistribution: CC BY 4.0

## 2. Description and research use cases

urban fleet transition; low-emission zones; mixed fleet; real road-distance case studies

Problem families: mixed-fleet EVRP, low-emission-zone routing, real-road case study.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `Schneider-derived EVRPTW base data` | Parent customer/depot/station and time-window data inherited from Schneider benchmark instances. |
| `LEZ centre and radius` | Geometric centre and boundary/radius of a low-emission zone; record coordinate system and vehicle access rules. |
| `vehicle fleet types` | Vehicle classes with different energy, emissions, capacity, access and operating cost attributes. |
| `Milan Area C real-road distances` | Road-network distance information for the Milan restricted zone case; distinguish from Euclidean distances. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "mixed_fleet_LEZ": "candidate_direct (schema validation pending)",
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
  --data data/raw --out reports --dataset EVRP-012
```

## 6. Primary citations

- Michael Schneider, Andreas Stenger, Dominik Goeke (2014). *The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations*. Transportation Science, 48(4), 500–520. https://doi.org/10.1287/trsc.2013.0490
- Maurizio Bruglieri, Bülent Çatay, Merve Keskin, Simona Mancini, Ornella Pisacane (2025). *The Mixed-Fleet Vehicle Routing Problem with Low Emission Zones*. Transportation Research Part E: Logistics and Transportation Review (dataset record: to appear). https://data.mendeley.com/datasets/np452gmj7f/2

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
