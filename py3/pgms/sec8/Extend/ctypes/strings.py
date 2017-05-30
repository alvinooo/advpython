#!/usr/bin/env python3
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

mystr = b'radar'
(mystr, num) = replace(mystr, b'r', b'm')
print("Number of changes = %s" %num)
print(mystr.decode("ascii"))

#####################################
#
#     $ strings.py
#     Number of changes = 2
#     madam
#
