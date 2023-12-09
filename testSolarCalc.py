from SolarCalc import SolarDate, Vector3d, Spherical3d
from datetime import date, timedelta

if __name__ == '__main__':
    test1s = Spherical3d(1.0, 60.0, -60.0)
    test1v = test1s.toCartesian()
    print(test1v.x, test1v.y, test1v.z,
          (test1v.x * test1v.x) + (test1v.y * test1v.y) + (test1v.z * test1v.z))
    test2v = Spherical3d(1.0, 90.0, 0.0).toCartesian() #1,0,0
    print(test2v.x, test2v.y, test2v.z)
    test3v = Spherical3d(1.0, 0.0, 0.0).toCartesian() #0,0,1
    print(test3v.x, test3v.y, test3v.z)
    test4v = Spherical3d(1.0, 90.0, 90.0).toCartesian() #0,1,0
    print(test4v.x, test4v.y, test4v.z)
    test5v = Spherical3d(1.0, 90.0, 30.0).toCartesian() #0.8,0.5,0
    print(test5v.x, test5v.y, test5v.z)
    test6v = Spherical3d(1.0, 60.0, 0.0).toCartesian() #0.8,0,0.5
    print(test6v.x, test6v.y, test6v.z)
    test6vr = test6v.rotateY(60.0) #
    print(test6vr.x, test6vr.y, test6vr.z)
    
