#!/usr/bin/env python3
# mycircle.py - Circle with properties
from Circle import Circle

c1 = Circle(10)              
print("radius = %g" %c1.radius)      # get property

c1.radius = 20                       # set property
print("radius = %g" %c1.radius)      # get property

c1.radius = -30                      # bad radius
print("radius = %g" %c1.radius)      # get property

#################################################
#
#    $ mycircle.py
#    radius = 10
#    radius = 20
#    Traceback (most recent call last):
#      File "./mycircle.py", line 11, in <module>
#        c1.radius = -30                      # bad radius
#      File "./advpython/py3/pgms/sec3/Circle.py", line 14, in radius
#        raise ValueError("Circle has bad radius %d" %radius)
#    ValueError: Circle has bad radius -30
#
