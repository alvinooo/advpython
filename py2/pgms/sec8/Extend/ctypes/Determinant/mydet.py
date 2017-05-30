#!/usr/bin/env python
# mydet.py - ctype conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

class MyStruct(Structure):
    _fields_ = [("array", (c_double * 4) * 4)]

# double getDeterminant(MyStruct *)
mylib.getDeterminant.argtypes = (POINTER(MyStruct),)
mylib.getDeterminant.restype = c_double

m = MyStruct()

# invoke C avg() function for lists or tuples
def det(array2d):
    rowcol = len(array2d)
    for row in range(rowcol):
        for col in range(rowcol):
            m.array[row][col] = array2d[row][col]
    return mylib.getDeterminant(byref(m))

# call C det() function
matrix = [ 
    [ 1, 3, 2, 1 ],
    [ 4, 6, 1, 2 ],
    [ 2, 1, 2, 3 ],
    [ 1, 2, 4, 1 ]]

print det(matrix)

#####################################
#
#     $ mydet.py
#     43.0
#
