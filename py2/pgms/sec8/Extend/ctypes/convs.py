#!/usr/bin/env python
# convs.py - ctype conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# double mult(double, double)
mylib.mult.argtypes = (c_double, c_double)
mylib.mult.restype = c_double

# call C mult() function
print mylib.mult(2.5, 3.5)

#####################################
#
#     $ convs.py
#     8.75
#
