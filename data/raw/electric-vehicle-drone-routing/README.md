# Electric vehicle-drone routing instances (adjacent family)

> **Dataset ID:** `EVRP-014`  
> **Published/expected instance count:** 128  
> **Problem family:** EV-drone routing, synchronised truck-drone routing  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://github.com/setyotw/EVDRP_instances
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: GitHub repository snapshot; README updated 2026-07-09
- Licence / redistribution: repository states CC0-1.0

## 2. Description and research use cases

EV-drone coordination; synchronization; integrated routing

Problem families: EV-drone routing, synchronised truck-drone routing.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `Schneider-derived EVRP nodes` | Parent benchmark node locations and types reused in the EV-drone routing dataset. |
| `drone service/synchronization attributes` | Drone launch/recovery, service time, rendezvous and synchronization fields linking drone sorties to vehicle routes. |
| `vehicle and drone operational parameters` | Vehicle/drone payload, battery, speed, endurance and operational availability; units and fleet definitions are source-specific. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EVDRP": "direct_fit",
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
  --data data/raw --out reports --dataset EVRP-014
```

## 6. Primary citations

- Setyo Tri Windras Mara, Ruhul Sarker, Daryl Essam, Saber Elsayed (2023). *Solving electric vehicle–drone routing problem using memetic algorithm*. Swarm and Evolutionary Computation, 79, 101295. https://doi.org/10.1016/j.swevo.2023.101295
- Michael Schneider, Andreas Stenger, Dominik Goeke (2014). *The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations*. Transportation Science, 48(4), 500–520. https://doi.org/10.1287/trsc.2013.0490

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-014`. The source-specific adapter is `github`.

- Source/version: [main (pin resolved commit)](https://github.com/setyotw/EVDRP_instances)
- Current redistribution gate: **verified**
- Automatic repository inclusion: **eligible after the runner re-verifies the source metadata and validation**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
