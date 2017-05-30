#!/usr/bin/env python
# limit.py - set a time limit on a process
import sys
from os import *
from signal import *

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s -sec command" %sys.argv[0])

try:
    cpid = fork()            # create child
    if cpid == 0:            # child
        execvp(sys.argv[2], sys.argv[2:])
    else:                    # parent
        signal(SIGALRM, lambda signo, frame : 
            kill(cpid, SIGKILL))         # stop process
        timeout = int(sys.argv[1][1:])   # timeout period
        alarm(timeout)                   # schedule alarm
        waitpid(cpid, 0)     # wait for child to finish
except Exception as ex:
    raise SystemExit("%s killed after %d seconds" 
        %(sys.argv[2], timeout))
    
###############################################
#
#    $ limit.py -10 sleep 5
#
#    $ limit.py -5 sleep 10
#    sleep killed after 5 seconds
# 
#    $ limit.py -10 find /usr -name "*.pyc"
#    find killed after 10 seconds
#
