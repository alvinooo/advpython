#!/usr/bin/env python
# structs.py - ctype structure conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# double slope(Point *, Point *)
mylib.slope.argtypes = (POINTER(Point), POINTER(Point))
mylib.slope.restype = c_double

# call C slope() function
p1 = Point(5, 10)
p2 = Point(2, 6)
print "%g" %mylib.slope(p1, p2)

#####################################
#
#     $ structs.py
#     1.33333
#
