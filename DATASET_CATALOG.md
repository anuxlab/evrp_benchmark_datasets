# EVRP Benchmark Dataset Catalogue

> Scope: diversified electric-routing benchmark datasets and adjacent electric mobility problem families. Registry entries are curated leads; only records marked locally ingested have been parsed in this repository.

## Evidence and ingestion labels

- **Research-published:** linked to a peer-reviewed publication or formal research paper.
- **Officially hosted:** source is the author, journal data repository, competition, Zenodo, Mendeley Data, VRP-REP or project repository.
- **Locally ingested:** archive is included in `data/raw/` and has been parsed by the current pipeline.
- **Schema pending:** source is discoverable and cited, but its files/units/fields have not yet been downloaded and inspected.
- **Compatibility candidate:** the source description suggests a variant fit; do not call it direct-fit until file-level validation is complete.

## Dataset catalogue

### EVRP-001 — Mavrovouniotis E-CVRP benchmark (current upstream listing)

- **Problem family:** E-CVRP, load-dependent energy E-CVRP
- **Official source:** https://github.com/Mavrovouniotis/e-cvrp_benchmark_instances
- **Dataset DOI/version:** 10.1109/CEC48606.2020.9185753; GitHub master snapshot; pin commit before experiments
- **Published instance count:** 24
- **Status:** research_published_and_officially_hosted | Licence: upstream repository terms must be checked before redistribution
- **Parameters:** coordinates, depot, customer demands, vehicle count, payload capacity, battery capacity, energy consumption, charging-station nodes, distance metric, published objective reference
- **Use cases:** c, l, a, s, s, i, c, a, l,  , E, -, C, V, R, P, ;,  , l, o, a, d, -, d, e, p, e, n, d, e, n, t,  , e, n, e, r, g, y, ;,  , c, h, a, r, g, i, n, g, -, s, t, a, t, i, o, n,  , d, e, n, s, i, t, y, ;,  , s, c, a, l, i, n, g,  , a, n, d,  , m, e, t, a, h, e, u, r, i, s, t, i, c,  , c, o, m, p, a, r, i, s, o, n
- **Compatibility:** `{"E-CVRP": "direct_fit", "EVRP": "direct_fit", "EVRPTW": "unsupported", "dynamic_price": "unsupported", "nonlinear_charging": "unsupported", "heterogeneous_fleet": "unsupported"}`
- **Citations:** P02
- **Notes:** The uploaded 17-file ZIP is a separate historical/local snapshot; do not label it as the current 24-instance upstream listing. Current upstream file list has 24 .evrp instances.

### EVRP-002 — Schneider-Goeke E-VRPTW instances

- **Problem family:** E-VRPTW, E-CVRPTW
- **Official source:** https://data.mendeley.com/datasets/h3mrm5dhxw/1
- **Dataset DOI/version:** 10.17632/h3mrm5dhxw.1; Version 1 (2019)
- **Published instance count:** 92
- **Status:** research_published_and_officially_hosted | Licence: CC BY-NC 3.0
- **Parameters:** node type, coordinates, demand, ready time, due date, service time, battery Q, load capacity C, energy rate r, inverse refueling rate g, speed v
- **Use cases:** t, i, m, e,  , w, i, n, d, o, w, s, ;,  , c, l, u, s, t, e, r, e, d, /, r, a, n, d, o, m, /, r, a, n, d, o, m, -, c, l, u, s, t, e, r, e, d,  , c, u, s, t, o, m, e, r,  , d, i, s, t, r, i, b, u, t, i, o, n, s, ;,  , E, V, R, P,  , b, a, s, e, l, i, n, e, s,  , a, n, d,  , c, h, a, r, g, i, n, g,  , p, o, l, i, c, y,  , e, x, p, e, r, i, m, e, n, t, s
- **Compatibility:** `{"EVRPTW": "direct_fit", "EVRP": "conditional_fit (relax time windows)", "E-CVRP": "direct_fit", "nonlinear_charging": "unsupported", "dynamic_price": "unsupported"}`
- **Citations:** P01
- **Notes:** The supplied archive contains 92 TXT instance files. Preserve the non-commercial restriction and cite both the dataset DOI and the 2014 paper.

### EVRP-003 — Montoya et al. nonlinear charging benchmark

- **Problem family:** E-VRP-NL
- **Official source:** https://www.vrp-rep.org/datasets/item/2016-0020.html
- **Dataset DOI/version:** No separate DOI recorded; VRP-REP ID 2016-0020
- **Published instance count:** 120
- **Status:** research_published_and_repository_catalogued | Licence: VRP-REP public listing; instance-level redistribution terms require source check
- **Parameters:** customer service times, charging stations, battery capacity, travel times, arc energy consumption, piecewise-linear concave charging curves, partial recharge decisions
- **Use cases:** n, o, n, l, i, n, e, a, r,  , c, h, a, r, g, i, n, g, ;,  , p, a, r, t, i, a, l,  , r, e, c, h, a, r, g, e, ;,  , c, o, m, p, a, r, i, s, o, n,  , o, f,  , c, h, a, r, g, i, n, g,  , m, o, d, e, l, s, ;,  , c, h, a, r, g, i, n, g, -, d, e, c, i, s, i, o, n,  , h, e, u, r, i, s, t, i, c, s
- **Compatibility:** `{"E-VRP-NL": "direct_fit", "linear_charging_EVRP": "conditional_fit (model simplification)", "E-VRPTW": "unsupported unless windows supplied"}`
- **Citations:** P03
- **Notes:** Official VRP-REP catalogue lists 120 instances. DIMACS identifies this as the E-VRP-NL base set. Retrieve exact files from VRP-REP/DIMACS source and validate.

### EVRP-004 — Froger capacitated charging-station variants

- **Problem family:** E-VRP-NL-C, capacitated charging stations
- **Official source:** https://dimacs.rutgers.edu/programs/implementation-challenges/vehicle-routing/implementation-challenge-vehicle-routing/electric-vehicle-routing-problem
- **Dataset DOI/version:** No separate DOI recorded; DIMACS challenge benchmark specification
- **Published instance count:** 240
- **Status:** research_published_and_competition_specified | Licence: follow VRP-REP/DIMACS distribution terms
- **Parameters:** Montoya base instance, charger capacity at each station (1 or 2 chargers), nonlinear charging curve, charging occupancy and queue interaction
- **Use cases:** s, t, a, t, i, o, n,  , c, o, n, g, e, s, t, i, o, n, ;,  , c, h, a, r, g, e, r, -, c, a, p, a, c, i, t, y,  , c, o, n, s, t, r, a, i, n, t, s, ;,  , n, o, n, l, i, n, e, a, r,  , c, h, a, r, g, i, n, g, ;,  , s, o, l, u, t, i, o, n,  , c, h, e, c, k, e, r,  , e, v, a, l, u, a, t, i, o, n
- **Compatibility:** `{"E-VRP-NL-C": "direct_fit", "E-VRP-NL": "conditional_fit (remove charger capacity constraints)"}`
- **Citations:** P03, P04
- **Notes:** These 240 are two derived capacity variants per each of the 120 Montoya instances; they are not 240 unrelated base instances. DIMACS reports 120 base + 240 derived = 360 total across both categories.

### EVRP-005 — Goeke-Schneider mixed-fleet EVRPTW-MF

- **Problem family:** EVRPTW-MF, mixed electric/ICE fleet
- **Official source:** https://data.mendeley.com/datasets/bd7rm5fw6k/1
- **Dataset DOI/version:** 10.17632/bd7rm5fw6k.1; Version 1 (2022)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** research_published_and_officially_hosted | Licence: CC BY 4.0
- **Parameters:** EV and conventional vehicle fleet types, time windows, speed, road gradient, cargo-load distribution, energy consumption
- **Use cases:** m, i, x, e, d,  , p, o, w, e, r, t, r, a, i, n,  , f, l, e, e, t, ;,  , f, l, e, e, t,  , a, l, l, o, c, a, t, i, o, n, ;,  , r, e, a, l, -, w, o, r, l, d,  , e, n, e, r, g, y,  , m, o, d, e, l, ;,  , m, i, x, e, d, -, f, l, e, e, t,  , r, o, u, t, i, n, g
- **Compatibility:** `{"EVRPTW-MF": "direct_fit", "homogeneous_EV": "conditional_fit (restrict fleet to EVs)", "ICE-EVRP": "direct_fit"}`
- **Citations:** P05, P12
- **Notes:** Mendeley record does not state a total instance count in the surfaced metadata; do not invent one.

### EVRP-006 — Felipe et al. GVRP multiple technologies and partial recharges

- **Problem family:** GVRP-MTPR, multiple charging technologies, partial recharge
- **Official source:** https://www.vrp-rep.org/datasets/item/2018-0004.html
- **Dataset DOI/version:** No separate DOI recorded; VRP-REP ID 2018-0004
- **Published instance count:** 41
- **Status:** research_published_and_repository_catalogued | Licence: VRP-REP public listing; source terms to be checked
- **Parameters:** multiple recharge technologies, station/technology compatibility, partial recharge amounts, vehicle autonomy, geographical instance attributes
- **Use cases:** p, a, r, t, i, a, l,  , r, e, c, h, a, r, g, e, ;,  , c, h, a, r, g, e, r,  , t, e, c, h, n, o, l, o, g, y,  , c, h, o, i, c, e, ;,  , m, i, x, e, d,  , c, h, a, r, g, i, n, g,  , i, n, f, r, a, s, t, r, u, c, t, u, r, e
- **Compatibility:** `{"GVRP-MTPR": "direct_fit", "single_technology_EVRP": "conditional_fit (restrict technology choices)"}`
- **Citations:** P06
- **Notes:** VRP-REP currently catalogues 41 instances; some review literature describes a 60-instance FORT collection. Treat the discrepancy as unresolved until the precise release/archive is reconciled; do not combine counts.

### EVRP-007 — Akbay et al. expanded two-echelon EVRP dataset

- **Problem family:** 2E-EVRP, 2E-EVRPTW, SPD, partial delivery
- **Official source:** https://zenodo.org/records/14844216
- **Dataset DOI/version:** 10.5281/zenodo.14844216; Version 2 (2025)
- **Published instance count:** 3000
- **Status:** research_published_and_officially_hosted | Licence: Zenodo record describes software/data release; verify archive-level licence before republishing
- **Parameters:** central depot, satellite depots, two vehicle echelons, customer coordinates and demand, time windows, EV battery and load capacities, SPD and partial delivery flags
- **Use cases:** t, w, o, -, e, c, h, e, l, o, n,  , l, o, g, i, s, t, i, c, s, ;,  , s, a, t, e, l, l, i, t, e, s, ;,  , t, i, m, e,  , w, i, n, d, o, w, s, ;,  , s, i, m, u, l, t, a, n, e, o, u, s,  , p, i, c, k, u, p, /, d, e, l, i, v, e, r, y, ;,  , p, a, r, t, i, a, l,  , d, e, l, i, v, e, r, i, e, s, ;,  , s, c, a, l, e,  , t, e, s, t, s
- **Compatibility:** `{"2E-EVRP": "direct_fit", "2E-EVRPTW": "direct_fit", "single_echelon_EVRP": "unsupported without documented projection"}`
- **Citations:** P07, P08
- **Notes:** Zenodo v2 states 3,000 instances. It is a distinct two-echelon family, not a single-echelon EVRP corpus.

### EVRP-008 — V2G and dynamic energy pricing extended EVRPTW

- **Problem family:** EVRPTW-V2G, time-of-use energy pricing
- **Official source:** https://data.mendeley.com/datasets/dmnhggw478/1
- **Dataset DOI/version:** 10.17632/dmnhggw478.1; Version 1 (2026)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** dataset_published_schema_not_yet_inspected | Licence: CC BY 4.0
- **Parameters:** base EVRPTW data, vehicle-to-grid capability, time-of-use energy tariffs, time-dependent charge/discharge decisions
- **Use cases:** e, n, e, r, g, y, -, c, o, s, t,  , o, p, t, i, m, i, z, a, t, i, o, n, ;,  , V, 2, G,  , r, e, v, e, n, u, e, ;,  , t, i, m, e, -, d, e, p, e, n, d, e, n, t,  , c, h, a, r, g, i, n, g, ;,  , g, r, i, d,  , i, n, t, e, r, a, c, t, i, o, n
- **Compatibility:** `{"EVRPTW-V2G-DP": "candidate_direct (schema validation pending)", "static_EVPR": "conditional_fit"}`
- **Citations:** P10
- **Notes:** Mendeley data record is available; inspect files and any linked paper before promoting compatibility to direct_fit.

### EVRP-009 — Gradient-aware EVRPTW with altitude information

- **Problem family:** EVRPTW-GR, gradient/load-dependent energy, regenerative braking
- **Official source:** https://data.mendeley.com/datasets/srfdbp2twv/1
- **Dataset DOI/version:** 10.17632/srfdbp2twv.1; Version 1 (2025)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** dataset_published_schema_not_yet_inspected | Licence: CC BY 4.0
- **Parameters:** Schneider base instance fields, altitude/elevation, road gradient, regenerative braking, load dynamics
- **Use cases:** g, r, a, d, e, -, a, w, a, r, e,  , e, n, e, r, g, y,  , u, s, e, ;,  , d, o, w, n, h, i, l, l,  , r, e, g, e, n, e, r, a, t, i, o, n, ;,  , r, e, a, l, i, s, t, i, c,  , e, n, e, r, g, y,  , m, o, d, e, l, l, i, n, g
- **Compatibility:** `{"EVRPTW-GR": "candidate_direct (schema validation pending)", "base_EVPRTW": "conditional_fit"}`
- **Citations:** P01, P09
- **Notes:** Dataset record explicitly describes modified Schneider instances; preserve parent-child derivation and inspect Description.docx for exact parameter units.

### EVRP-010 — Charging-station energy differences

- **Problem family:** EVRP heterogeneous station energy
- **Official source:** https://data.mendeley.com/datasets/4ktbt29z5x/1
- **Dataset DOI/version:** 10.17632/4ktbt29z5x.1; Version 1 (2023)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** dataset_published_schema_not_yet_inspected | Licence: CC BY 4.0
- **Parameters:** station-specific energy differences/attributes (exact fields in README)
- **Use cases:** h, e, t, e, r, o, g, e, n, e, o, u, s,  , c, h, a, r, g, i, n, g,  , s, t, a, t, i, o, n,  , e, n, e, r, g, y,  , c, h, a, r, a, c, t, e, r, i, s, t, i, c, s, ;,  , s, t, a, t, i, o, n, -, c, h, o, i, c, e,  , s, e, n, s, i, t, i, v, i, t, y
- **Compatibility:** `{"EVRP-station-energy": "candidate_direct (schema validation pending)"}`
- **Citations:** P11
- **Notes:** Mendeley record describes three distinct data sets/configurations, not necessarily three individual problem instances. Inspect readme.txt before formal parameter mapping.

### EVRP-011 — EVRP with backhauls and time windows under uncertainty (EVRPBTW-USUT)

- **Problem family:** EVRPBTW-USUT, backhauls, time windows, uncertain travel/service times
- **Official source:** https://datadryad.org/dataset/doi:10.5061/dryad.6hdr7srbv
- **Dataset DOI/version:** 10.5061/dryad.6hdr7srbv; Dryad version 2025
- **Published instance count:** 60
- **Status:** research_dataset_hosted_schema_not_yet_inspected | Licence: Dryad dataset terms to be checked
- **Parameters:** backhaul demand, time windows, travel-time uncertainty, service-time uncertainty, deterministic and robust solutions, real case network/time/distance matrices
- **Use cases:** r, o, b, u, s, t, /, s, t, o, c, h, a, s, t, i, c,  , r, o, u, t, i, n, g, ;,  , b, a, c, k, h, a, u, l,  , o, p, e, r, a, t, i, o, n, s, ;,  , d, e, t, e, r, m, i, n, i, s, t, i, c, -, v, s, -, r, o, b, u, s, t,  , m, e, t, h, o, d, s, ;,  , r, e, a, l, -, c, a, s, e,  , v, a, l, i, d, a, t, i, o, n
- **Compatibility:** `{"EVRPBTW-USUT": "candidate_direct (archive parser pending)", "standard_EVPRTW": "conditional_fit"}`
- **Citations:** P14
- **Notes:** The GitHub README describes 60 synthetic instances (25/50/100 customers) plus a 47-customer real case. Counts should be rechecked against archive manifest before validation.

### EVRP-012 — Mixed-fleet VRP with low-emission zones (EVRPTW-derived + Milan case)

- **Problem family:** mixed-fleet EVRP, low-emission-zone routing, real-road case study
- **Official source:** https://data.mendeley.com/datasets/np452gmj7f/2
- **Dataset DOI/version:** 10.17632/np452gmj7f.2; Version 2 (2025)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** research_published_and_officially_hosted | Licence: CC BY 4.0
- **Parameters:** Schneider-derived EVRPTW base data, LEZ centre and radius, vehicle fleet types, Milan Area C real-road distances
- **Use cases:** u, r, b, a, n,  , f, l, e, e, t,  , t, r, a, n, s, i, t, i, o, n, ;,  , l, o, w, -, e, m, i, s, s, i, o, n,  , z, o, n, e, s, ;,  , m, i, x, e, d,  , f, l, e, e, t, ;,  , r, e, a, l,  , r, o, a, d, -, d, i, s, t, a, n, c, e,  , c, a, s, e,  , s, t, u, d, i, e, s
- **Compatibility:** `{"mixed_fleet_LEZ": "candidate_direct (schema validation pending)", "base_EVPRTW": "conditional_fit"}`
- **Citations:** P01, P13
- **Notes:** This is a derived dataset: cite both the dataset DOI and its paper, and explicitly acknowledge Schneider et al. as the parent benchmark.

### EVRP-013 — Electric autonomous dial-a-ride benchmark (adjacent family)

- **Problem family:** eADARP, electric dial-a-ride, ride-pooling
- **Official source:** https://github.com/claudiabongiovanni/eADARP
- **Dataset DOI/version:** No separate DOI recorded; GitHub repository snapshot; pin commit
- **Published instance count:** Not stated / not independently confirmed
- **Status:** research_published_and_author_hosted | Licence: repository licence/file terms should be checked
- **Parameters:** requests/origins/destinations, time windows and ride-time constraints, depots, charging stations, vehicle capacities, initial battery inventory, recharge rates, Uber-derived travel times
- **Use cases:** o, n, -, d, e, m, a, n, d,  , m, o, b, i, l, i, t, y, ;,  , p, a, s, s, e, n, g, e, r,  , r, o, u, t, i, n, g, ;,  , r, i, d, e, -, p, o, o, l, i, n, g, ;,  , b, a, t, t, e, r, y, -, c, o, n, s, t, r, a, i, n, e, d,  , D, A, R, P
- **Compatibility:** `{"eADARP": "direct_fit", "freight_EVPRTW": "not_applicable"}`
- **Citations:** P15, P16
- **Notes:** Adjacent electric mobility benchmark, not a freight EVRP dataset. Include in a separate problem-family collection.

### EVRP-014 — Electric vehicle-drone routing instances (adjacent family)

- **Problem family:** EV-drone routing, synchronised truck-drone routing
- **Official source:** https://github.com/setyotw/EVDRP_instances
- **Dataset DOI/version:** No separate DOI recorded; GitHub repository snapshot; README updated 2026-07-09
- **Published instance count:** 128
- **Status:** research_published_and_author_hosted | Licence: repository states CC0-1.0
- **Parameters:** Schneider-derived EVRP nodes, drone service/synchronization attributes, vehicle and drone operational parameters
- **Use cases:** E, V, -, d, r, o, n, e,  , c, o, o, r, d, i, n, a, t, i, o, n, ;,  , s, y, n, c, h, r, o, n, i, z, a, t, i, o, n, ;,  , i, n, t, e, g, r, a, t, e, d,  , r, o, u, t, i, n, g
- **Compatibility:** `{"EVDRP": "direct_fit", "freight_EVPRTW": "not_applicable"}`
- **Citations:** P17, P01
- **Notes:** 128 instances adapted from Schneider et al. Cite Mara et al. (2023) for EVDRP and Schneider et al. (2014) as the parent benchmark source. Separate adjacent problem family, not standard EVRP.

### EVRP-015 — EM-DARP electric shuttle demand-responsive routing dataset (adjacent family)

- **Problem family:** electric mobility DARP, electric shuttle routing, demand-responsive transport
- **Official source:** https://zenodo.org/records/23468137
- **Dataset DOI/version:** 10.5281/zenodo.23468137; Version 1 (2026-10-19)
- **Published instance count:** Not stated / not independently confirmed
- **Status:** recent_zenodo_release_schema_not_yet_inspected | Licence: verify exact Zenodo record licence before redistribution
- **Parameters:** benchmark_instances.csv, benchmark_instances.json, benchmark_instances.tex, electric shuttle routing parameters (inspect release metadata)
- **Use cases:** electric shuttle and demand-responsive routing, mobility-oriented DARP research, adjacent electric fleet benchmarks
- **Compatibility:** `{"EM-DARP": "candidate_direct (dataset files and associated paper need inspection)", "freight_EVPRTW": "not_applicable"}`
- **Citations:** Dataset landing page only; primary paper citation not yet verified
- **Notes:** New adjacent dataset published 19 October 2026. It is a DARP/mobility dataset, not a conventional freight EVRP benchmark; retain as a separate family.

## Reference records

### P01 — The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations
- Michael Schneider, Andreas Stenger, Dominik Goeke (2014). *The Electric Vehicle-Routing Problem with Time Windows and Recharging Stations*. Transportation Science, 48(4), 500–520.
- Type: research_publication
- DOI: 10.1287/trsc.2013.0490
- Link: https://doi.org/10.1287/trsc.2013.0490

### P02 — A Benchmark Test Suite for the Electric Capacitated Vehicle Routing Problem
- Michalis Mavrovouniotis, Charalambos Menelaou, Stelios Timotheou, Georgios Ellinas, Christos Panayiotou, Marios Polycarpou (2020). *A Benchmark Test Suite for the Electric Capacitated Vehicle Routing Problem*. 2020 IEEE Congress on Evolutionary Computation, 1–8.
- Type: research_publication
- DOI: 10.1109/CEC48606.2020.9185753
- Link: https://doi.org/10.1109/CEC48606.2020.9185753

### P03 — The electric vehicle routing problem with nonlinear charging function
- Alejandro Montoya, Christelle Guéret, Jorge E. Mendoza, Juan G. Villegas (2017). *The electric vehicle routing problem with nonlinear charging function*. Transportation Research Part B: Methodological, 103, 87–110.
- Type: research_publication
- DOI: 10.1016/j.trb.2017.02.004
- Link: https://doi.org/10.1016/j.trb.2017.02.004

### P04 — The Electric Vehicle Routing Problem with Capacitated Charging Stations
- Aurélien Froger, Ola Jabali, Jorge E. Mendoza, Gilbert Laporte (2022). *The Electric Vehicle Routing Problem with Capacitated Charging Stations*. Transportation Science, 56(2), 460–482.
- Type: research_publication
- DOI: 10.1287/trsc.2021.1111
- Link: https://doi.org/10.1287/trsc.2021.1111

### P05 — Routing a mixed fleet of electric and conventional vehicles
- Dominik Goeke, Michael Schneider (2015). *Routing a mixed fleet of electric and conventional vehicles*. European Journal of Operational Research, 245(1), 81–99.
- Type: research_publication
- DOI: 10.1016/j.ejor.2015.01.049
- Link: https://doi.org/10.1016/j.ejor.2015.01.049

### P06 — A heuristic approach for the green vehicle routing problem with multiple technologies and partial recharges
- Ángel Felipe, M. Teresa Ortuño, Giovanni Righini, Gregorio Tirado (2014). *A heuristic approach for the green vehicle routing problem with multiple technologies and partial recharges*. Transportation Research Part E: Logistics and Transportation Review, 71, 111–128.
- Type: research_publication
- DOI: 10.1016/j.tre.2014.09.003
- Link: https://doi.org/10.1016/j.tre.2014.09.003

### P07 — Variable neighborhood search for the two-echelon electric vehicle routing problem with time windows
- Mehmet Anıl Akbay, Çağrı B. Kalaycı, Christian Blum, Oya Polat (2022). *Variable neighborhood search for the two-echelon electric vehicle routing problem with time windows*. Applied Sciences, 12(3), 1014.
- Type: research_publication
- DOI: 10.3390/app12031014
- Link: https://doi.org/10.3390/app12031014

### P08 — A dataset for two-echelon electric vehicle routing problems
- Mehmet Anıl Akbay, Christian Blum (2025). *A dataset for two-echelon electric vehicle routing problems*. Data in Brief, 60, 111470.
- Type: data_article
- DOI: 10.1016/j.dib.2025.111470
- Link: https://doi.org/10.1016/j.dib.2025.111470

### P09 — Uphill Struggles, Downhill Gains: How Road Gradients and Load Dynamics Influence Electric Vehicle Routing Decisions?
- Sina Rastani, Merve Keskin, Tugce Yuksel, Bülent Çatay (2025). *Uphill Struggles, Downhill Gains: How Road Gradients and Load Dynamics Influence Electric Vehicle Routing Decisions?*. European Journal of Operational Research (dataset record describes article as to appear).
- Type: research_publication
- DOI: No DOI verified
- Link: https://data.mendeley.com/datasets/srfdbp2twv/1

### P10 — Extended Benchmark Instances for the Electric Vehicle Routing Problem with V2G and Dynamic Energy Pricing
- Luis Fernando Rodriguez Jimenez (2026). *Extended Benchmark Instances for the Electric Vehicle Routing Problem with V2G and Dynamic Energy Pricing*. Mendeley Data, Version 1.
- Type: dataset_record
- DOI: 10.17632/dmnhggw478.1
- Link: https://doi.org/10.17632/dmnhggw478.1

### P11 — Data for: Electric vehicle routing problem considering energy differences of charging stations
- Lijun Fan (2023). *Data for: Electric vehicle routing problem considering energy differences of charging stations*. Mendeley Data, Version 1.
- Type: dataset_record
- DOI: 10.17632/4ktbt29z5x.1
- Link: https://doi.org/10.17632/4ktbt29z5x.1

### P12 — EVRPTW-MF
- Dominik Goeke, Michael Schneider (2022). *EVRPTW-MF*. Mendeley Data, Version 1.
- Type: dataset_record
- DOI: 10.17632/bd7rm5fw6k.1
- Link: https://doi.org/10.17632/bd7rm5fw6k.1

### P13 — The Mixed-Fleet Vehicle Routing Problem with Low Emission Zones
- Maurizio Bruglieri, Bülent Çatay, Merve Keskin, Simona Mancini, Ornella Pisacane (2025). *The Mixed-Fleet Vehicle Routing Problem with Low Emission Zones*. Transportation Research Part E: Logistics and Transportation Review (dataset record: to appear).
- Type: research_publication
- DOI: No DOI verified
- Link: https://data.mendeley.com/datasets/np452gmj7f/2

### P14 — Routing short-haul trucks under the uncertainties of travel time and service time
- Dongbo Peng, Kanok Boriboonsomsin, Matthew Barth (2025). *Routing short-haul trucks under the uncertainties of travel time and service time*. Dryad dataset and associated EVRPBTW-USUT study.
- Type: research_publication
- DOI: 10.5061/dryad.6hdr7srbv
- Link: https://doi.org/10.5061/dryad.6hdr7srbv

### P15 — The electric autonomous dial-a-ride problem
- Claudia Bongiovanni, Moshe Kaspi, Nikolas Geroliminis (2019). *The electric autonomous dial-a-ride problem*. Transportation Research Part B: Methodological, 122, 436–456.
- Type: research_publication
- DOI: No DOI verified
- Link: https://github.com/claudiabongiovanni/eADARP

### P16 — Survey of charging management and infrastructure planning for electrified demand-responsive transport systems: Methodologies and recent developments
- Tai-Yu Ma, Yumeng Fang (2022). *Survey of charging management and infrastructure planning for electrified demand-responsive transport systems: Methodologies and recent developments*. European Transport Research Review, 14, article 36.
- Type: research_publication
- DOI: 10.1186/s12544-022-00560-3
- Link: https://doi.org/10.1186/s12544-022-00560-3

### P17 — Solving electric vehicle–drone routing problem using memetic algorithm
- Setyo Tri Windras Mara, Ruhul Sarker, Daryl Essam, Saber Elsayed (2023). *Solving electric vehicle–drone routing problem using memetic algorithm*. Swarm and Evolutionary Computation, 79, 101295.
- Type: research_publication
- DOI: 10.1016/j.swevo.2023.101295
- Link: https://doi.org/10.1016/j.swevo.2023.101295
