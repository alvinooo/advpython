#!/usr/bin/env python3
# addr.py - ctype address conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# void myfunc(double *)
mylib.myfunc.argtypes = (POINTER(c_double),)
mylib.myfunc.restype = None

# call C myfunc() function
dval = c_double(0.0)                 # create double
result = mylib.myfunc(byref(dval))   # invoke myfunc(&dval)
print(dval.value)

dval = c_double(5.0)                 # create double
ptr = pointer(dval)                  # create pointer
result = mylib.myfunc(ptr)           # invoke myfunc(ptr)
print(dval.value)                     # inspect value

########################################
#
#     $ addr.py
#     3.45
#     3.45
#
