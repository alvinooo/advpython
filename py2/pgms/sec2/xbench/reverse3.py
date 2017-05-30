#!/usr/bin/env python
# reverse3.py - reverse lines in a file, fastest
import sys

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

file = open(sys.argv[1], "r+")
flist = file.readlines()
flist.reverse()

file.seek(0, 0)
file.writelines(flist)
file.close()

###############################################
#
#    $ reverse3.py testfile
#    real     0m0.214s
#    user     0m0.120s
#    sys      0m0.072s
# 
