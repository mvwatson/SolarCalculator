import json
# solaryear describes a summer solstice (northern hemisphere) year for the purpose of calculating the tilt angle for any other date
solaryear = {"start": "2021-12-21", "end": "2022-12-21"}

# dates for the calculation can either be an aray of dates or parameters for generating the dates
datearray = ["2021-12-21", "2022-01-21", "2022-02-21", "2022-03-21", "2022-04-21", "2022-05-21", "2022-06-21",
           "2022-07-21", "2022-08-21", "2022-09-21", "2022-10-21", "2022-11-21", "2022-12-21"]

daterange = {"start": "2021-12-21", "end": "2022-06-21", "days": 1}

timerange = {"start": 5, "end": 19}

# the calculated results are bucketed to accumlate into time buckets and also day buckets
# for example 5 minute calculations bucketed for an hour and daily calculations into monthly buckets
# that would give an approximately 12x12 grid of results
output = {"secondincrement": 300, "secondbucket":  3600, "daybucket": 7}

data = {"solaryear": solaryear,
        "daterange": daterange,
        "timerange": timerange,
        "output": output}

f = open("dateparams.json", "w")
f.write(json.dumps(data, indent=4))
f.close()
