#!/usr/bin/env python3
# reverse1.py - reverse lines in a file, slow
import sys
from os import *
from mmap import *

if (len(sys.argv) != 2):
    raise SystemExit("Usage: %s file" %sys.argv[0])

filename = sys.argv[1]
len = path.getsize(filename)       # get file length
infd = open(filename, O_RDONLY)
outfd = open("temp", O_WRONLY | O_CREAT, 0o666)

buf = mmap(infd, len, MAP_PRIVATE, PROT_READ) 

nbytes = 1
for cur in range(len-2, -1, -1):
    if buf[cur] == 0xA:            # check for '\n' byte
        write(outfd, buf[cur+1:cur+nbytes+1])
        nbytes = 0
    nbytes += 1
write(outfd, buf[:cur+nbytes])

buf.close()                            # unmap memory
close(infd); close(outfd)              # close filescrs
rename("temp", filename)               # rename file 

###############################################
#
#    $ time reverse1.py data
#    real     0m8.088s
#    user     0m4.464s
#    sys      0m3.212s
# 
