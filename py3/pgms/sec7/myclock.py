#!/usr/bin/env python3
# myclock.py - clock daemon thread
import sys
from threading import *
from time import *
from logging import *
basicConfig(level=ERROR, format="(%(threadName)s) %(message)s",)

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s interval" %sys.argv[0])

interval = float(sys.argv[1])    # time interval

def doSomething():
    sleep(5*interval)            # doing something...

def myClock(nap):
    debug("clock started...")
    while (True):
        print(ctime())
        sleep(nap)

try:
    clock = Thread(target=myClock, args=(interval,))
    clock.daemon = True         # daemon clock thread
    clock.start()               # start daemon running
    doSomething()
except KeyboardInterrupt:
    sys.exit(1)                 # stop program
finally:
    debug("stopped")

##################################################
#
#     $ myclock.py 1
#     Mon Jan 23 15:31:44 2017
#     Mon Jan 23 15:31:45 2017
#     Mon Jan 23 15:31:46 2017
#     Mon Jan 23 15:31:47 2017
#     Mon Jan 23 15:31:48 2017
#
