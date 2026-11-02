# EVRP with backhauls and time windows under uncertainty (EVRPBTW-USUT)

> **Dataset ID:** `EVRP-011`  
> **Published/expected instance count:** 60  
> **Problem family:** EVRPBTW-USUT, backhauls, time windows, uncertain travel/service times  
> **Local status:** Catalogued source; original instance files are not yet vendored in this repository.

## 1. Official source and version

- Official source: https://datadryad.org/dataset/doi:10.5061/dryad.6hdr7srbv
- Dataset DOI: 10.5061/dryad.6hdr7srbv
- Version/snapshot: Dryad version 2025
- Licence / redistribution: Dryad dataset terms to be checked

## 2. Description and research use cases

robust/stochastic routing; backhaul operations; deterministic-vs-robust methods; real-case validation

Problem families: EVRPBTW-USUT, backhauls, time windows, uncertain travel/service times.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `backhaul demand` | Pickup/collection quantity, often served after delivery; preserve precedence and capacity accounting. |
| `time windows` | Permitted service-start or service interval at a customer; verify the exact semantics of earliest/latest service. |
| `travel-time uncertainty` | Random, interval or scenario-based variation in travel duration; retain distributions/scenarios and seeds. |
| `service-time uncertainty` | Uncertainty in customer service duration; retain distribution and scenario assumptions. |
| `deterministic and robust solutions` | Reference solutions under nominal inputs and uncertainty-aware/robust formulations; compare like-for-like objective definitions. |
| `real case network/time/distance matrices` | Network-based arc data from a real case; record matrix units, directedness and mapping from nodes to real locations. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "EVRPBTW-USUT": "candidate_direct (archive parser pending)",
  "standard_EVPRTW": "conditional_fit"
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
  --data data/raw --out reports --dataset EVRP-011
```

## 6. Primary citations

- Dongbo Peng, Kanok Boriboonsomsin, Matthew Barth (2025). *Routing short-haul trucks under the uncertainties of travel time and service time*. Dryad dataset and associated EVRPBTW-USUT study. https://doi.org/10.5061/dryad.6hdr7srbv

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.

## Automated acquisition

This collection can be selected in the manually triggered GitHub Actions workflow **Dataset acquisition** using `EVRP-011`. The source-specific adapter is `dryad`.

- Source/version: [2025-07-02](https://datadryad.org/dataset/doi:10.5061/dryad.6hdr7srbv)
- Current redistribution gate: **manual_review**
- Automatic repository inclusion: **disabled pending explicit maintainer rights review**

A successful download alone does not change the repository's integrated-dataset or validated-instance counts. See [`acquisition/README.md`](../../../acquisition/README.md) for adapter details, validation, issue handling and the source-specific legal gate.
