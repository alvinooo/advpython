#!/usr/bin/env python3
# defaults.py - default ctypes
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# int greeting(char *)
mylib.greeting(b'bob')

# int add(int, int)
print(mylib.add(2, 3))

#####################################
#
#     $ defaults.py
#     hello there, bob
#     5
#
