from SolarCalc import SolarDate, Vector3d, Spherical3d
from math import radians
import json
from datetime import date, datetime, timedelta, time
from multiprocessing import Pool
from itertools import accumulate
import operator


def calcDay(nextDay):
    print(nextDay)
    f = open("location.json")
    panelData = json.loads(f.read())
    f.close()
    f = open("dateparams.json")
    dateData = json.loads(f.read())
    f.close()
    vectorLocation = Spherical3d(rho = 1.0, theta = 90.0 - panelData.get("location").get("latitude"),
                                 phi = 0.0).toCartesian()
    panels = []
    for panel in panelData.get("panels"):
        panels.append({"name": panel.get("name"),
                       "spherical": Spherical3d(1.0, panel.get("theta"),
                                  panel.get("phi")).toCartesian()
                      .rotateY(panelData.get("location").get("latitude") - 90.0),
                       "power": panel.get("power")})
    datecalc = SolarDate(dateData.get("solaryear").get("start"), dateData.get("solaryear").get("end"))
    sun = Spherical3d(1.0, 90.0 - datecalc.calcTiltAngleDays(nextDay), 0.0)
    secondincrement = dateData.get("output").get("secondincrement")
    secondbucket = dateData.get("output").get("secondbucket")
    paneltotal = {"day": nextDay, "timebucket": secondbucket} # {"day": int, "timebucket": int, "panelpower": [{"name": str, "starttime": int, "timepower": [float]}]}
    # Accumulate results into buckets
    starttime = dateData.get("timerange").get("start") * 3600 # 5am
    endtime = dateData.get("timerange").get("end") * 3600 + 1 # 7pm plus an extra second
    panelpower = []
    for panel in panels:
        timepower = {"name": panel.get("name"), "starttime": starttime}
        timetotal = []
        panelbucket = 0.0
        bucket = 0
        for nextTime in range(starttime, endtime, secondincrement):
            sun.phi = radians(float(43200 - (nextTime - (secondincrement / 2))) / 240.0) # 12 noon is 0, +ve is am, -ve is pm
            vectorSun = sun.toCartesian()
            locsun = vectorSun.dotProduct(vectorLocation)
            panelsun = vectorSun.dotProduct(panel.get("spherical")) if locsun > 0.0 else 0.0
            panelbucket += panelsun if panelsun > 0.0 else 0.0
            bucket += secondincrement
            if bucket == secondbucket:
                timetotal.append(panelbucket * float(secondincrement) / 3600.0 * panel["power"])
                panelbucket = 0.0
                bucket = 0
        timepower["timepower"] = timetotal
        panelpower.append(timepower)
    paneltotal["panelpower"] = panelpower
    return paneltotal

##def daterange(date1, date2, delta):
##    for n in range(int ((date2 - date1).days)+1):
##        yield date1 + timedelta(delta)

if __name__ == '__main__':
    print("Start", datetime.now())
    f = open("dateparams.json")
    dateData = json.loads(f.read())
    f.close()

    startdays = (date.fromisoformat(dateData.get("daterange").get("start")) - date.fromisoformat(dateData.get("solaryear").get("start"))).days
    print(startdays)
    daybucket = dateData.get("output").get("daybucket")
    totalPower = 0.0
    with Pool(processes=4) as pool:
        # results will contain an dict of time-bucketed power quantities per panel
        # for example, 4 panels with hourly buckets would be a dict of 4 where each
        # element was a list of 24 values plus a 5th string for the name of the result
        results = pool.map(calcDay, range((date.fromisoformat(dateData.get("daterange").get("start"))
                           - date.fromisoformat(dateData.get("solaryear").get("start"))).days,
                          (date.fromisoformat(dateData.get("daterange").get("end"))
                           - date.fromisoformat(dateData.get("daterange").get("start"))).days,
                          int(dateData.get("daterange").get("days"))))
        # the results are by day
        # [{"day": int, "timebucket": int, "panelpower": [{"name": str, "starttime": int, "timepower": [float]}]}]
        for res in results:
            print(date.fromisoformat(dateData.get("daterange").get("start")) + timedelta(days=res["day"]), res["timebucket"])
            for panel in res["panelpower"]:
                sumpower = sum(panel["timepower"])
                totalPower += sumpower
                print(panel["name"], timedelta(seconds=panel["starttime"]), panel["timepower"], sumpower)
        print(totalPower)
        # Bucket results by the daybucket value. Restructure the bucketed results by panel
        # and add a totals array. Add a totals element to each panel dict for the day.
        # [{"name": str, "panelday": [{"bucketday": int, "timebucket": int, "starttime": int, "timepower": [float], "totalpower": float}], "totalpower": float}}]
        bucket = 0
        panelpower = []
        for dayres in results:
            panelray = []
            for panel in dayres["panelpower"]:
                curr = {"name": panel["name"]}
                panelday = {"bucketday": dayres["day"], "timebucket": dayres["timebucket"], "starttime": panel["starttime"]}
                
            bucket += 1
            if bucket == daybucket:
                bucket = 0
        #panelpower.append(timepower)
    print("End", datetime.now())



