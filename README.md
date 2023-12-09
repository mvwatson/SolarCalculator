# SolarCalculator

This repository holds a set of programs to deal with calculating how much solar radiation (insolation) shines on surfaces on Earth.

More instructions later but, for now, edit dateparams.json (if needed) and location.json (with your panel details) and run CalcTotal.py.

The approach is to compute the dot product of two unit vectors. One vector is the normal to the solar panel, the other is towards the sun. 
The sun vector is computed based on time of day and the date. The rest is just multiplication and addition.

For the location settings, latitude represents north of the equator, theta the angle away from north and phi is tilt towards the south. 
All in degrees for input purposes.

TODO:

More options for aggregating the time buckets.

Output in OBJ format so the data can be visualised, e.g. Blender.
