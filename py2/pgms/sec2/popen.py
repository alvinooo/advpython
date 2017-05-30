#!/usr/bin/env python
# popen.py - simulates popen()
import sys
from os import *
BUFSIZE = 1024

stdout = sys.stdout.fileno()   # get file descriptor
(pipein, pipeout) = pipe()     # create pipe

pid = fork()                   # create child process
if pid != 0:                   # parent reads from pipe
    close(pipeout)             # close parent write end
    while True:
        data = read(pipein, BUFSIZE)   # read data
        if not data: break     # no more data
        write(stdout, data)    # write data to stdout
    close(pipein)              # close parent read end
else:                          # child writes to pipe
    close(pipein)              # close child read end
    dup2(pipeout, stdout)      # make writing end stdout 
    execlp("date", "date")     # run date command

###############################################
#
#    $ popen.py
#    Wed Oct 19 11:46:06 PDT 2016
# 
