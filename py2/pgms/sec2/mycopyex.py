#!/usr/bin/env python
# mycopyex.py - copy files, exception handling
import sys, traceback
from os import *
BUFSIZE = 1024

if (len(sys.argv) != 3):
    raise SystemExit("Usage: %s file1 file2" %sys.argv[0])

try:
    fd1 = open(sys.argv[1], O_RDONLY)
    fd2 = open(sys.argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644)
    while True:
        data = read(fd1, BUFSIZE)      # read data
        if not data: break             # no more data
        write(fd2, data)               # write data
    close(fd1)
    close(fd2)
except Exception as ex:
    traceback.print_exc()
    sys.exit(1)

###############################################
#
#    $ mycopyex.py
#    Usage: ./mycopyex.py file1 file2
#
#    $ mycopyex.py f1 file2
#    Traceback (most recent call last):
#      File "./mycopyex.py", line 11, in <module>
#        f1 = open(sys.argv[1], O_RDONLY)
#    OSError: [Errno 2] No such file or directory: 'f1'
#
#    $ mycopyex.py file1 /etc/passwd
#    Traceback (most recent call last):
#      File "./mycopyex.py", line 12, in <module>
#        f2 = open(sys.argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644)
#    OSError: [Errno 13] Permission denied: '/etc/passwd'
#
#    $ mycopyex.py file1 file2
#     
