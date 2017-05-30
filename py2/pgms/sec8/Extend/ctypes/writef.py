#!/usr/bin/env python
# writef.py - write file with clib
from ctypes import *

# load shared C library
mylib = CDLL("libc.so.6")

# open file for writing
fp = mylib.fopen("filedata", "w")
mydata = "Here is some data.\n"
print "writing filedata"
mylib.fwrite(mydata, len(mydata), 1, fp)
mylib.fclose(fp)

#####################################
#
#     $ writef.py
#     writing filedata
#
