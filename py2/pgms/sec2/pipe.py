#!/usr/bin/env python
# pipe.py - parent and child pipe
import sys
from os import *
BUFSIZE = 1024

stdout = sys.stdout.fileno()   # get file descriptor
(pipein, pipeout) = pipe()     # create pipe

pid = fork()                   # create process
if pid != 0:                   # parent writes to pipe
    close(pipein)              # close parent read end
    write(pipeout, "Here's a message...\n")
    close(pipeout)             # done writing
    wait()                     # wait for child to finish
else:                          # child reads from pipe
    close(pipeout)             # close child write end
    while True:
        data = read(pipein, BUFSIZE)   # read data
        if not data: break     # no more data
        write(stdout, data)    # write data to stdout
    close(pipein)              # close child read end

###############################################
#
#    $ pipe.py
#    Here's a message...
# 
