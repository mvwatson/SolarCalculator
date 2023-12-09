import json
# attenuation: response cutoff, atmospheric reduction and monthly cloud loss

response = {"cutoff": 0.01}

atmospheric = {"maxreduction": 0.1}

cloudiness = [{"month": 1, "loss": 0.15},
              {"month": 2, "loss": 0.15},
              {"month": 3, "loss": 0.15},
              {"month": 4, "loss": 0.1},
              {"month": 5, "loss": 0.1},
              {"month": 6, "loss": 0.1},
              {"month": 7, "loss": 0.1},
              {"month": 8, "loss": 0.1},
              {"month": 9, "loss": 0.1},
              {"month": 10, "loss": 0.1},
              {"month": 11, "loss": 0.1},
              {"month": 12, "loss": 0.15}]

data = {"response": response,
        "atmospheric": atmospheric,
        "cloudiness": cloudiness}

f = open("attenuation.json", "w")
f.write(json.dumps(data, indent=4))
f.close()
