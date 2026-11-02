# Froger capacitated charging-station variants

> **Dataset ID:** `EVRP-004`  
> **Published/expected instance count:** 240  
> **Problem family:** E-VRP-NL-C, capacitated charging stations  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://dimacs.rutgers.edu/programs/implementation-challenges/vehicle-routing/implementation-challenge-vehicle-routing/electric-vehicle-routing-problem
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: DIMACS challenge benchmark specification
- Licence / redistribution: follow VRP-REP/DIMACS distribution terms

## 2. Description and research use cases

station congestion; charger-capacity constraints; nonlinear charging; solution checker evaluation

Problem families: E-VRP-NL-C, capacitated charging stations.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `Montoya base instance` | Parent nonlinear-charging benchmark instance from which station-capacity variants are derived. |
| `charger capacity at each station (1 or 2 chargers)` | Number of vehicles that may charge simultaneously at a station; this creates a resource/occupancy constraint. |
| `nonlinear charging curve` | Non-constant charging rate / nonlinear mapping between SOC and charging time or energy. |
| `charging occupancy and queue interaction` | Station resource contention and possible waiting caused by finite simultaneous charging capacity. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "E-VRP-NL-C": "direct_fit",
  "E-VRP-NL": "conditional_fit (remove charger capacity constraints)"
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
  --data data/raw --out reports --dataset EVRP-004
```

## 6. Primary citations

- Alejandro Montoya, Christelle Guéret, Jorge E. Mendoza, Juan G. Villegas (2017). *The electric vehicle routing problem with nonlinear charging function*. Transportation Research Part B: Methodological, 103, 87–110. https://doi.org/10.1016/j.trb.2017.02.004
- Aurélien Froger, Ola Jabali, Jorge E. Mendoza, Gilbert Laporte (2022). *The Electric Vehicle Routing Problem with Capacitated Charging Stations*. Transportation Science, 56(2), 460–482. https://doi.org/10.1287/trsc.2021.1111

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-004`. The source-specific adapter is `dimacs_derived`.

- Source/version: [DIMACS E-VRP-NL-C challenge specification](https://dimacs.rutgers.edu/programs/implementation-challenges/vehicle-routing/implementation-challenge-vehicle-routing/electric-vehicle-routing-problem)
- Current redistribution gate: **manual_review**
- Automatic repository inclusion: **disabled pending explicit maintainer rights review**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
