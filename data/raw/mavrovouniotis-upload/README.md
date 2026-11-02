# Mavrovouniotis E-CVRP benchmark (current upstream listing)

> **Dataset ID:** `EVRP-001`  
> **Published/expected instance count:** 24  
> **Problem family:** E-CVRP, load-dependent energy E-CVRP  
> **Local status:** Locally ingested; parser validation passed for 17 supplied instances.

## 1. Official source and version

- Official source: https://github.com/Mavrovouniotis/e-cvrp_benchmark_instances
- Dataset DOI: No separate dataset DOI recorded; cite the source publication / official repository.
- Version/snapshot: GitHub master snapshot; pin commit before experiments
- Licence / redistribution: upstream repository terms must be checked before redistribution

## 2. Description and research use cases

classical E-CVRP; load-dependent energy; charging-station density; scaling and metaheuristic comparison

Problem families: E-CVRP, load-dependent energy E-CVRP.

## 3. Parameters and characteristics

| Parameter / source field | Explanation and modelling caution |
|---|---|
| `coordinates` | Node location values used to calculate travel distance or travel time. Confirm whether coordinates are Euclidean, road-network or geographic and record the coordinate reference system. |
| `depot` | The route start/end facility; record depot count and whether routes must return to the same depot. |
| `customer demands` | Required delivery or collection quantity at each customer; preserve sign convention and payload unit. |
| `vehicle count` | Fleet availability or maximum number of routes/vehicles; distinguish a hard fleet limit from a suggested value. |
| `payload capacity` | Maximum carried load per vehicle; record whether vehicle types have different capacities. |
| `battery capacity` | Maximum usable onboard energy / state-of-charge capacity; retain source energy units and initial SOC assumptions. |
| `energy consumption` | Energy required to traverse an arc; determine whether it depends on distance, speed, vehicle load, road grade or vehicle type. |
| `charging-station nodes` | Locations where vehicles can recharge; coordinates alone do not specify plug count, power, queues or charging curve. |
| `distance metric` | Rule used to compute arc distance (e.g. Euclidean, rounded Euclidean or road-network matrix); must match published benchmark convention. |
| `published objective reference` | Published best-known/optimal objective value or bound; store objective definition and do not call a bound an optimum. |

Parameter units are source-specific. The canonical schema must retain the original symbol, source unit, normalized field, any conversion formula and whether the value is source-provided, derived or assumed.


## 4. Problem-variant eligibility

```json
{
  "E-CVRP": "direct_fit",
  "EVRP": "direct_fit",
  "EVRPTW": "unsupported",
  "dynamic_price": "unsupported",
  "nonlinear_charging": "unsupported",
  "heterogeneous_fleet": "unsupported"
}
```

Compatibility means the source is potentially suitable based on available fields. It does not certify feasibility or guarantee that the currently implemented parser supports this format.

## 5. Local files and use

This repository currently contains **17** locally ingested instance files for this source snapshot under this folder. These are the user-supplied archive snapshot, not automatically assumed to be the latest upstream release.

Run validation:

```bash
PYTHONPATH=src python -m evrp_bench.runner \
  --data data/raw \
  --out reports \
  --dataset EVRP-001
```

List actual files in this folder (excluding this README) to identify available instances. Preserve their original filenames.

## 6. Primary citations

- Michalis Mavrovouniotis, Charalambos Menelaou, Stelios Timotheou, Georgios Ellinas, Christos Panayiotou, Marios Polycarpou (2020). *A Benchmark Test Suite for the Electric Capacitated Vehicle Routing Problem*. 2020 IEEE Congress on Evolutionary Computation, 1–8. https://doi.org/10.1109/CEC48606.2020.9185753

## 7. Citation requirement

When using this dataset, cite the original dataset and primary paper above. If you also use this curated repository, cite **EVRP Benchmark Datasets** as described in the root `CITATION.cff` and `docs/CITATION_AND_PROVENANCE.md`.
