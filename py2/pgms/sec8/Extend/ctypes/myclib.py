# myclib.py - ctypes module
from ctypes import *

mylib = CDLL("./mylib.so")         # load shared library

def greeting(arg):
    return mylib.greeting(arg)     # int greeting(char *)

def add(a, b):
    return mylib.add(a, b)         # int add(int, int)

# double mult(double, double)
mylib.mult.argtypes = (c_double, c_double)
mylib.mult.restype = c_double

def mult(a, b):
    return mylib.mult(a, b)

# int divide(int, int, int *)
mylib.divide.argtypes = (c_int, c_int, POINTER(c_int))

def divide(a, b):
    remainder = c_int()
    result = mylib.divide(9, 4, remainder)
    return (result, remainder.value)
    
# double avg(double *, int)
mylib.avg.argtypes = (POINTER(c_double), c_int)
mylib.avg.restype = c_double

# invoke C avg() function for lists or tuples
def avg(seq):
    size = len(seq)
    doubleArray = (c_double * size)(*seq)
    return mylib.avg(doubleArray, size)

# int replace(char *, char, char)
mylib.replace.argtypes = (c_char_p, c_char, c_char)

# call C replace() function
def replace(string, oldch, newch):
    sbuf = create_string_buffer(string)
    nrep = mylib.replace(sbuf, oldch, newch)
    return (sbuf.value, nrep)

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]

# double slope(Point *, Point *)
mylib.slope.argtypes = (POINTER(Point), POINTER(Point))
mylib.slope.restype = c_double

def slope(p1, p2):
    return mylib.slope(p1, p2)
