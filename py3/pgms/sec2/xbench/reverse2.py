#!/usr/bin/env python3
# reverse2.py - reverse lines in a file, faster
import sys
from os import *
from mmap import *

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

filename = sys.argv[1]
len = path.getsize(filename)       # get file length
infd = open(filename, O_RDONLY)
outfd = open("temp", O_RDWR | O_CREAT | O_TRUNC, 0o644)
ftruncate(outfd, len)                 # set file length

buf1 = mmap(infd, len, MAP_PRIVATE, PROT_READ) 
buf2 = mmap(outfd, len, MAP_SHARED, PROT_WRITE)

nbytes = 1; start = 0
for cur in range(len-2, -1, -1):
    if buf1[cur] == 0xA:           # check for '\n' byte
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
#    real     0m3.720s
#    user     0m3.472s
#    sys      0m0.048s
# 
