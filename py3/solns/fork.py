#!/usr/bin/env python3
# fork.py - create children, report when done
import os
from time import sleep
from errno import *

naptime = (5, 12, 3, 19, 7)

def birth(n):
    nap = naptime[n]
    cpid = os.fork()            # create child
    if cpid == 0:               # child
        sleep(nap)
        os._exit(nap)
    print("Gave birth to %d...sleeping for %d secs" %(cpid, nap))

for n in range(0, 5):
    birth(n)

try:
    while True:
        (pid, status) = os.wait()
        if os.WIFEXITED(status):
            print("Child process %d has slept for %d seconds" \
                %(pid, os.WEXITSTATUS(status)))

except OSError as ex:
    if ex.errno == ECHILD:
        print("All children are done.")

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
