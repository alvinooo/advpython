#!/usr/bin/env python
# myClockObj.py - Clock thread object
import sys
from time import sleep 
from Clock import Clock

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s interval" %sys.argv[0])

interval = float(sys.argv[1])      # time interval
def doSomething(): 
    sleep(5*interval)              # doing something

try:
    clock = Clock(interval)        # Clock object
    clock.start()                  # start Clock
    doSomething()                  # do something
except KeyboardInterrupt:
    sys.exit(1)                    # stop program
finally:
    clock.cancel()                 # stop Clock

##################################################
#
#     $ myClockObj.py 1
#     Mon Jan 23 15:31:44 2017
#     Mon Jan 23 15:31:45 2017
#     Mon Jan 23 15:31:46 2017
#     Mon Jan 23 15:31:47 2017
#     Mon Jan 23 15:31:48 2017
#
