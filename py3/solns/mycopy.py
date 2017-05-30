#!/usr/bin/env python3
# mycopy.py - copy files
import sys
from os import *
from mmap import *

if (len(sys.argv) != 3):
    raise SystemExit("Usage: %s file1 file2" %sys.argv[0])

flen = path.getsize(sys.argv[1])     # get file length

fd1 = open(sys.argv[1], O_RDONLY)
fd2 = open(sys.argv[2], O_RDWR | O_CREAT | O_TRUNC, 0o644)
ftruncate(fd2, flen)                 # set file length

buf1 = mmap(fd1, flen, MAP_PRIVATE, PROT_READ)
buf2 = mmap(fd2, flen, MAP_SHARED, PROT_WRITE)

buf2[:] = buf1[:]                    # copy all data

buf1.close(); buf2.close()          # unmap memory
close(fd1); close(fd2)              # close files

###############################################
#
#    $ mycopy.py
#    Usage: ./mycopy.py file1 file2
#
#    $ mycopy.py file1 file2
#     
