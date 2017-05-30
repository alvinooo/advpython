#!/usr/bin/env python3
# mymap.py - memory mapped IO
import sys
from os import *
from mmap import *

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

file = sys.argv[1]
flen = path.getsize(file)       # get file length
fd = open(file, O_RDWR)

buf = mmap(fd, flen, MAP_SHARED, PROT_READ | PROT_WRITE) 
print(buf[:])                  # show all lines
buf[:] = buf[:].upper()        # convert to uppercase
buf.close()                    # unmap memory
close(fd)                      # close file

###############################################
#
#    $ mymap.py numlines
#    this is line one.
#    this is line two.
#    this is line three.
# 
#    $ cat numlines
#    THIS IS LINE ONE.
#    THIS IS LINE TWO.
#    THIS IS LINE THREE.
#
