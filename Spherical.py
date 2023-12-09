from math import radians, sin, cos

class Spherical:
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
        return tuple((self.rho * cosphi * sintheta, self.rho * sinphi * sintheta, self.rho * costheta))

    def dotProduct(self, other):
        a = self.toCartesian()
        b = other.toCartesian()
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    
    

unit = 1.0
latitude = -25.0
tropic = 23.5
summer = Spherical(unit, 90.0 + tropic, 0.0)
winter = Spherical(unit, 90.0 - tropic, 0.0)
equinox = Spherical(unit, 90.0, 0.0)
location = Spherical(unit, 90.0 - latitude, 0.0)
panelNorth1 = Spherical(unit, 90.0 - latitude - 40.0, 5.0)
panelNorth2 = Spherical(unit, 90.0 - latitude - 17.5, 5.0)
panelEast = Spherical(unit, 90.0 - latitude - 40.0, 95.0)
panelWest = Spherical(unit, 90.0 - latitude - 40.0, -85.0)
print(panelEast.toCartesian())
txt = "{0}: S {1:.3f} W {2:.3f} E {3:.3f}"
print(txt.format("Location", location.dotProduct(summer), location.dotProduct(equinox), location.dotProduct(winter)))
print(txt.format("North 1", panelNorth1.dotProduct(summer), panelNorth1.dotProduct(equinox), panelNorth1.dotProduct(winter)))
print(txt.format("North 2", panelNorth2.dotProduct(summer), panelNorth2.dotProduct(equinox), panelNorth2.dotProduct(winter)))
print(txt.format("East", panelEast.dotProduct(summer), panelEast.dotProduct(equinox), panelEast.dotProduct(winter)))
print(txt.format("West", panelWest.dotProduct(summer), panelWest.dotProduct(equinox), panelWest.dotProduct(winter)))


