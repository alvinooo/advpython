#!/usr/bin/env python
# forkwait.py - parent and child processes
import os 
from time import sleep

print("Parent process is %d" %os.getpid())

cpid = os.fork()         # create child
if cpid == 0:            # child
    print "Child process %d sleeping..." %os.getpid()
    sleep(3)
    os._exit(77)
else:                    # parent
    (pid, status) = os.waitpid(cpid, 0)
    if os.WIFEXITED(status):
        print "Child process %d exited with %d" \
            %(pid, os.WEXITSTATUS(status))
    
###############################################
#
#    $ forkwait.py
#    Parent process is 7257
#    Child process 7258 sleeping...
#    Child process 7258 exited with 77
# 
