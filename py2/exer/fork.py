#!/usr/bin/env python
# fork.py - create children, report when done
import os 
from time import sleep
from errno import *

BUFSIZE = 1024

naptime = (5, 12, 3, 19, 7)

# your code here...
for time in naptime:
    pid = os.fork()
    if pid == 0:
        sleep(time)
        os._exit(time)
    else:
        print "Gave birth to {0}...sleeping for {1} secs".format(pid, time)
        # pid, _ = os.waitpid(pid, 0)
        # print "Child process {0} has slept for {1} seconds".format(pid, time)
if pid != 0:
    for _ in naptime:
        pid, stat = os.wait()
        print "Child process {0} has slept for {1} seconds".format(pid, os.WEXITSTATUS(stat))

###############################################
#
#    $ fork.py
#    Gave birth to 7406...sleeping for 5 secs
#    Gave birth to 7407...sleeping for 12 secs
#    Gave birth to 7408...sleeping for 3 secs
#    Gave birth to 7409...sleeping for 19 secs
#    Gave birth to 7410...sleeping for 7 secs
#    Child process 7408 has slept for 3 seconds
#    Child process 7406 has slept for 5 seconds
#    Child process 7410 has slept for 7 seconds
#    Child process 7407 has slept for 12 seconds
#    Child process 7409 has slept for 19 seconds
#    All children are done.
# 
