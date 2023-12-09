import json

location = {"latitude": -25.0}
panels = [{"name": "North1",
           "theta": -40.0,
           "phi": -5.0,
           "power": 2.96},
          {"name": "North2",
           "theta": -17.5,
           "phi": -5.0,
           "power": 2.96},
          {"name": "East",
           "theta": -40.0,
           "phi": -95.0,
           "power": 1.448},
          {"name": "West",
           "theta": -40.0,
           "phi": 85.0,
           "power": 2.59}]
data = {"location": location,
        "panels": panels}

f = open("location.json", "w")
f.write(json.dumps(data, indent=4))
f.close()
