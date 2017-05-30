#!/usr/bin/env python
# reverse2.py - reverse lines in a file, faster
import sys
from os import *
from mmap import *

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

filename = sys.argv[1]
flen = path.getsize(filename)       # get file length
infd = open(filename, O_RDONLY)
outfd = open("temp", O_RDWR | O_CREAT | O_TRUNC, 0644)
ftruncate(outfd, flen)                 # set file length

buf1 = mmap(infd, flen, MAP_PRIVATE, PROT_READ) 
buf2 = mmap(outfd, flen, MAP_SHARED, PROT_WRITE)

nbytes = 1; start = 0
for cur in range(flen-2, -1, -1):
    if buf1[cur] == "\n":
        buf2[start:start+nbytes] = buf1[cur+1:cur+nbytes+1]
        start += nbytes
        nbytes = 0
    nbytes += 1
buf2[start:] = buf1[:cur+nbytes]

buf1.close(); buf2.close()             # unmap memory
close(infd); close(outfd)              # close files
rename("temp", filename)               # rename file 

###############################################
#
#    $ reverse2.py testfile
#    real     0m3.641s
#    user     0m3.324s
#    sys      0m0.156s
# 
