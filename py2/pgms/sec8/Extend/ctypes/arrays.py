#!/usr/bin/env python
# arrays.py - ctype array conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# double avg(double *, int)
mylib.avg.argtypes = (POINTER(c_double), c_int)
mylib.avg.restype = c_double

# invoke C avg() function for lists or tuples
def avg(seq):
    size = len(seq)
    doubleArray = (c_double * size)(*seq)
    return mylib.avg(doubleArray, size)
    
mylist = [1,2,3,4,5,6,7,8,9,10]
print avg(mylist)
    
mytuple = (5,6,7,8,9,10)
print avg(mytuple)

#####################################
#
#     $ arrays.py
#     5.5
#     7.5
#
