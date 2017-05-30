#!/usr/bin/env python
# mycopy.py - copy files
import sys
from os import *
from mmap import *

if (len(sys.argv) != 3):
    raise SystemExit("Usage: %s file1 file2" %sys.argv[0])

# your code here...
f1 = open(sys.argv[1], O_RDONLY)
f2 = open(sys.argv[2], O_RDWR | O_CREAT | O_TRUNC, 0644)
size = path.getsize(sys.argv[1])

ftruncate(f2, size)

buf1 = mmap(f1, size, MAP_SHARED, PROT_READ)
buf2 = mmap(f2, size, MAP_SHARED, PROT_WRITE)

buf2[:] = buf1[:]
buf1.close()
buf2.close()
close(f1)
close(f2)

###############################################
#
#    $ mycopy.py
#    Usage: ./mycopy.py file1 file2
#
#    $ mycopy.py file1 file2
#     
