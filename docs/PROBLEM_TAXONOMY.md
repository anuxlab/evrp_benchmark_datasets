# EVRP problem taxonomy and dataset eligibility

Compatibility is assessed by required mathematical attributes, not by filename or dataset title. The registry uses `direct_fit`, `conditional_fit`, `candidate_direct`, `unsupported`, and `not_applicable`. `candidate_direct` must not be upgraded until actual files, units and parameter semantics are inspected.

| Family | Required information / structure | Suitable benchmark leads |
|---|---|---|
| EVRP / E-CVRP | depot, customers, demands, payload capacity, battery, energy use, charging stations | Mavrovouniotis; Schneider (time windows may be relaxed explicitly) |
| EVRPTW | EVRP core + customer ready/due times and service times | Schneider; mixed-fleet derivatives |
| EVRPTW partial recharge | state-of-charge and continuous recharge amount/time decision | Keskin-Çatay derivatives of Schneider; Montoya nonlinear charging |
| EVRP-NL | nonlinear/piecewise charging-time-to-SoC function | Montoya 120-instance benchmark |
| EVRP-NL-C | EVRP-NL + finite charger count / station occupancy | Froger/DIMACS 240 derived variants |
| Load-dependent energy | load profile and load-sensitive arc energy | Mavrovouniotis E-CVRP; Goeke-Schneider mixed fleet; gradient dataset |
| Multiple charging technologies | station technology type, compatibility, charging rate/cost | Felipe et al. GVRP-MTPR |
| Heterogeneous powertrain fleet | per-type EV/ICE attributes and fleet availability | Goeke-Schneider EVRPTW-MF; LEZ dataset |
| Gradient-aware EVRP | elevation/grade by node or arc; regenerative braking model | Rastani et al. gradient dataset |
| Dynamic price / V2G | time-indexed tariff, charge/discharge power, SOC bounds, grid export rules | Rodriguez Jimenez 2026 dataset |
| Heterogeneous station energy | station-specific energy/price/charging attributes | Fan 2023 dataset |
| Two-echelon EVRP | central depot, satellites, echelon-specific vehicles and flows | Akbay et al. 2E-EVRP |
| Backhaul / uncertainty EVRP | pickup/backhaul demand, stochastic or robust travel/service parameters | Peng et al. EVRPBTW-USUT |
| Low-emission-zone routing | zone geometry, vehicle eligibility/emissions, fleet mix, network distances | Bruglieri et al. MFVRP-LEZ |
| Electric dial-a-ride | passenger pickup/drop-off, ride time, time windows, capacity, SOC | Bongiovanni et al. eADARP (adjacent family) |
| EV-drone routing | drone launch/recovery, synchronization, payload/range, EV energy | EVDRP_instances (adjacent family) |

## Rules for fair comparisons

- Relaxing time windows, reducing fleet types, or removing station capacities creates a *derived experiment configuration*. Record the transformation; do not label it as the unmodified original benchmark.
- Adding dynamic prices, nonlinear charging, gradients, or heterogeneous vehicle attributes creates a derived dataset unless the source already contains those fields.
- A dataset with only station coordinates does not directly support station capacity, queues, power limits, or time-varying tariffs.
- A homogeneous fleet dataset does not directly support heterogeneous fleet optimization.
- Two-echelon, DARP, EV-drone and freight EVRP are related but distinct families. Keep them separately filterable.
