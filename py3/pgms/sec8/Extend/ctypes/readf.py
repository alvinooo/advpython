#!/usr/bin/env python3
# readf.py - read file with clib
from ctypes import *
MAX = 1024

# load shared C library
mylib = CDLL("libc.so.6")

# open file for reading
fp = mylib.fopen(b'filedata', "r")
sbuf = create_string_buffer(MAX)
print("reading filedata")
mylib.fread(sbuf, MAX, 1, fp)
print(sbuf.value.decode("ascii"), end = '')
mylib.fclose(fp)

#####################################
#
#     $ readf.py
#     reading filedata
#     Here is some data.
#
