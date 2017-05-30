#!/usr/bin/env python3
# sortarray.py - sort C array of ints
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

mylib.sortArray.argtypes = (c_int, POINTER(c_int))
mylib.sortArray.restype = None

def sortArray(seq):
    size = len(seq)
    array = (c_int * size)(*seq)
    mylib.sortArray(size, array)
    return list(array)

# call C sortArray() function
nums = [7, 0, 8, 4, 3, 6, 9, 1, 5, 2]
nums = sortArray(nums)
print(nums)

#####################################
#
#     $ sortarray.py
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
