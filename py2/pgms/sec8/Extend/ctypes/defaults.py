#!/usr/bin/env python
# defaults.py - default ctypes
from ctypes import *

mylib = CDLL("./mylib.so")    # load shared library
mylib.greeting("bob")         # int greeting(char *)
print mylib.add(2, 3)         # int add(int, int)

############################################
#
#     $ defaults.py
#     hello there, bob
#     5
#
