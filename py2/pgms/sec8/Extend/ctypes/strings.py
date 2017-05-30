#!/usr/bin/env python
# strings.py - ctype string conversions
from ctypes import *

# load shared library
mylib = CDLL("./mylib.so")

# int replace(char *, char, char)
mylib.replace.argtypes = (c_char_p, c_char, c_char)

# call C replace() function
def replace(string, oldch, newch):
    sbuf = create_string_buffer(string)
    nrep = mylib.replace(sbuf, oldch, newch)
    return (sbuf.value, nrep)

mystr = "radar"
(mystr, num) = replace(mystr, "r", "m")
print "Number of changes = %s" %num
print mystr

#####################################
#
#     $ strings.py
#     Number of changes = 2
#     madam
#
