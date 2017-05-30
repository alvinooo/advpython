#!/usr/bin/env python3
# mycopy.py - copy files
import sys
from os import *
BUFSIZE = 1024

if (len(sys.argv) != 3):
    raise SystemExit("Usage: %s file1 file2" %sys.argv[0])

fd1 = open(sys.argv[1], O_RDONLY)
fd2 = open(sys.argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0o644)
while True:
    data = read(fd1, BUFSIZE)       # read data
    if not data: break              # no more data
    write(fd2, data)                # write data
close(fd1)
close(fd2)

###############################################
#
#    $ mycopy.py
#    Usage: ./mycopy.py file1 file2
#
#    $ mycopy.py f1 file2
#    Traceback (most recent call last):
#      File "./mycopy.py", line 11, in <module>
#        f1 = open(sys.argv[1], O_RDONLY)
#    OSError: [Errno 2] No such file or directory: 'f1'
#
#    $ mycopy.py file1 /etc/passwd
#    Traceback (most recent call last):
#      File "./mycopy.py", line 12, in <module>
#        f2 = open(sys.argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644)
#    OSError: [Errno 13] Permission denied: '/etc/passwd'
#
#    $ mycopy.py file1 file2
#     
