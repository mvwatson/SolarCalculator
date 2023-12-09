from math import radians, sin, cos, pi
from datetime import date, timedelta

class SolarDate:
    def __init__(self, startDate, endDate):
        # Date parameters are ISO strings "yyyy-mm-dd" and should represent a full year as a cosine curve
        self.startDate = date.fromisoformat(startDate)
        self.endDate = date.fromisoformat(endDate)
        self.days = int((self.endDate - self.startDate).days)
        self.tiltAngle = 23.5
    def calcTiltAngle(self, calcDate):
        angle = ((date.fromisoformat(calcDate) - self.startDate).days) / self.days * 2.0 * pi
        return self.tiltAngle * -cos(angle)
    def calcTiltAngleDays(self, calcDays):
        angle = calcDays / self.days * 2.0 * pi
        return self.tiltAngle * -cos(angle)

class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def rotateY(self, angledeg):
        angle = radians(angledeg)
        sinangle = sin(angle)
        cosangle = cos(angle)
        return Vector3d(self.x * cosangle - self.z * sinangle, self.y,
                        self.x * sinangle + self.z  * cosangle)
    def dotProduct(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def toString(self):
        txt = "X {0:.3f} Y {1:.3f} Z {2:.3f}"
        return txt.format(self.x, self.y, self.z)

class Spherical3d:    
    def __init__(self, rho, theta, phi):
        # Input angles are in degrees, stored in radians
        self.rho = rho
        self.theta = radians(theta)
        self.phi = radians(phi)
    def toCartesian(self):
        costheta = cos(self.theta)
        sintheta = sin(self.theta)
        cosphi = cos(self.phi)
        sinphi = sin(self.phi)
        return Vector3d(self.rho * cosphi * sintheta, self.rho * sinphi * sintheta, self.rho * costheta)
    def toString(self):
        txt = "rho {0:.3f} theta {1:.3f} phi {2:.3f}"
        return txt.format(self.rho, self.theta, self.phi)

if __name__ == '__main__':
    dateRay = ["2021-12-21", "2022-01-21", "2022-02-21", "2022-03-21", "2022-04-21", "2022-05-21", "2022-06-21",
               "2022-07-21", "2022-08-21", "2022-09-21", "2022-10-21", "2022-11-21", "2022-12-21"]
    unit = 1.0
    latitude = -25.0

    datecalc = SolarDate(dateRay[0], dateRay[len(dateRay) - 1])
    print(datecalc.days)
    location = Spherical3d(1.0, 90.0 - latitude, 0.0)
    print("Loc:", location.toCartesian().toString())
    panelNorth1 = Spherical3d(1.0, -40.0, -5.0)
    vectorNorth1 = panelNorth1.toCartesian().rotateY(latitude - 90.0)
    print("Nth:", vectorNorth1.toString())
    sun = Spherical3d(1.0, 0.0, 0.0)
    for nextDate in dateRay:
        print(nextDate, datecalc.calcTiltAngle(nextDate))
        sun.theta = radians(90.0 - datecalc.calcTiltAngle(nextDate))
        for nextTime in range(105, -120, -15):
            sun.phi = radians(float(nextTime))
            vectorSun = sun.toCartesian()
            print("Sun", nextTime, vectorSun.toString())
            print("Loc", nextTime, vectorSun.dotProduct(location.toCartesian()))
            print("Nth1", nextTime, vectorSun.dotProduct(vectorNorth1))
