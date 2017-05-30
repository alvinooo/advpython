#!/usr/bin/env python3
# reverse3.py - reverse lines in a file, fastest
import sys

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

file = open(sys.argv[1], "r+")
list = file.readlines()
list.reverse()

file.seek(0, 0)
file.writelines(list)
file.close()

###############################################
#
#    $ reverse3.py testfile
#    real     0m1.234s
#    user     0m1.064s
#    sys      0m0.104s
# 
