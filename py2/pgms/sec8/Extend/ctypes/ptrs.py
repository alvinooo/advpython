#!/usr/bin/env python
# ptrs.py - ctype pointer conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# int divide(int, int, int *)
mylib.divide.argtypes = (c_int, c_int, POINTER(c_int))

# call C divide() function
remainder = c_int()
print "division = %d " %mylib.divide(9, 4, remainder)
print "remainder = %d " %remainder.value

#####################################
#
#     $ ptrs.py
#     division = 2 
#     remainder = 1 
#
