# Dataset parameter dictionary (cross-family)

The same symbol can mean different things across papers. Always store source symbol, normalized field, unit, and source definition together. Do not assume common units across corpora.

| Normalized concept | Common symbols / names | Definition | Validation questions |
|---|---|---|---|
| Node identity/type | id, StringID, Type | Stable node identifier and role (depot/customer/station/satellite) | Unique IDs? Are node classes disjoint? |
| Coordinates | x, y, lat, lon | Spatial location | Cartesian or geographic? Coordinate reference system? |
| Demand | q_i, demand | Delivery/pickup quantity | Units? Signed pickup/delivery? |
| Time window | [a_i,b_i], ReadyTime, DueDate | Service start/finish bounds | Is due date latest start or completion? |
| Service duration | s_i, ServiceTime | Customer service time | Time units? |
| Vehicle load capacity | C, capacity | Payload upper bound | Same for all vehicles? |
| Battery capacity | Q, E_max | Maximum stored energy | kWh or normalized units? |
| Initial state of charge | E_0, SOC_0 | Battery energy at route start | Full, fixed, or decision variable? |
| Energy consumption | r, e_ij | Energy used on an arc | Distance-only, load-dependent, grade-aware? |
| Charging curve | phi_j(t), g | Charging time to SoC relation or inverse rate | Linear, piecewise-linear, nonlinear? Station-specific? |
| Charger capacity | m_j, plugs_j | Concurrent charging slots at station | Is waiting/queueing modelled? |
| Electricity tariff | p_j(t) | Price per unit energy at station/time | Currency and energy unit? Buy/sell tariff? |
| V2G power | P_dis, discharge_rate | Vehicle-to-grid export capability | Power limits, efficiency, SOC floor? |
| Elevation/grade | z_i, grade_ij | Road altitude or slope | Node/arc data? Sign convention? |
| Fleet type | k, vehicle_type | Vehicle technology and attributes | Per-type capacity, battery, cost, availability? |
| Satellite/echelon | satellite_id, echelon | Intermediate depot and stage | Which vehicle types serve each echelon? |
| Pickup/backhaul | pickup_i, backhaul_i | Reverse flow or collection demand | Simultaneous or separate service? |
| Uncertainty | scenarios, distributions, intervals | Stochastic/robust travel, service, or demand | Scenario weights and random seed? |

## Parameter provenance labels

- `source`: explicitly present in original source.
- `derived`: computed deterministically from source fields (document formula and units).
- `assumed`: introduced by the experimenter (must be exposed in config).
- `missing`: not available; never silently impute.
