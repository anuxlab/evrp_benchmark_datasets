def assess(r: dict) -> list[dict]:
    """Conservative eligibility; distinguishes direct evidence from assumptions."""
    if r["format"] == "mavrovouniotis_evrp":
        return [
          {"problem":"EVRP", "status":"direct_fit", "reason":"Coordinates, depot, customer demands, charging stations, battery and energy consumption are represented."},
          {"problem":"E-CVRP", "status":"direct_fit", "reason":"Cargo capacity and customer demands are represented."},
          {"problem":"EVRPTW", "status":"not_supported", "reason":"Customer time-window fields are absent."},
          {"problem":"EVRP with dynamic electricity pricing", "status":"conditional_fit", "reason":"Requires externally supplied time-dependent prices and charging-time decisions; neither is encoded."},
          {"problem":"EVRP with nonlinear/partial charging", "status":"conditional_fit", "reason":"Requires an added charging model; instance files do not specify nonlinear charging curves or partial-charge policy."},
          {"problem":"Heterogeneous-fleet EVRP", "status":"not_supported", "reason":"One common vehicle capacity/energy profile is supplied."},
          {"problem":"Multi-depot / pickup-delivery / two-echelon EVRP", "status":"not_supported", "reason":"No multi-depot, pickup, satellite, or echelon attributes are defined."},
        ]
    return [
      {"problem":"EVRPTW", "status":"direct_fit", "reason":"Customer ready/due times and service times, depot, charging stations, demand, battery and energy/refueling parameters are present."},
      {"problem":"EVRP", "status":"direct_fit", "reason":"Core EV routing, demand, depot, charging and energy attributes are present; time windows can be ignored for a relaxed EVRP experiment."},
      {"problem":"E-CVRP", "status":"direct_fit", "reason":"Demand and vehicle load capacity are supplied."},
      {"problem":"EVRPTW with partial/full recharge", "status":"conditional_fit", "reason":"Can be evaluated under explicitly selected charging policy; original data specifies an inverse refueling rate but does not itself prescribe every policy variant."},
      {"problem":"Dynamic electricity pricing", "status":"conditional_fit", "reason":"Add a documented time-of-use tariff; no price series is included."},
      {"problem":"Nonlinear charging / load-dependent energy", "status":"not_supported", "reason":"Linear inverse refueling rate and constant consumption parameter only."},
      {"problem":"Heterogeneous fleet / multi-depot / pickup-delivery / two-echelon", "status":"not_supported", "reason":"Required fleet, depot, pickup and echelon attributes are not represented."},
    ]
