#!/usr/bin/env python
# sortarray.py - sort C array of ints
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# your code here...
def sortArray(nums):
    size = len(nums)
    mylib.sortArray.argtypes = (c_int, POINTER(c_int))
    array = (c_int * size)(*nums)
    mylib.sortArray.restype = None
    mylib.sortArray(size, array)
    return list(array)

# call C sortArray() function
nums = [7, 0, 8, 4, 3, 6, 9, 1, 5, 2]
nums = sortArray(nums)
print nums

#####################################
#
#     $ sortarray.py
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
