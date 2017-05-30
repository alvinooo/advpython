#!/usr/bin/env python3
# mytimer.py - periodic timer as closure
import sys
from subprocess import call
from signal import *

def myTimer(timePeriod, func):
    def alarmHandler(signo,frame):         # signal handler
        func()
        alarm(timePeriod)                  # reschedule alarm
    def mywork():
        signal(SIGALRM, alarmHandler)      # register handler
        alarm(timePeriod)                  # schedule alarm
    return mywork

def doThis():
    call("date")                           # run date command
    #print("working...")

timer = myTimer(1, doThis)                 # create Timer
timer()                                    # start timer
print("timer running...")

try:
    while True:
        pass
except KeyboardInterrupt:                  # handle ctrl-C
    sys.exit(1)

#####################################
#
#     $ mytimer.py
#     timer running...
#     Thu Oct 20 11:45:10 PDT 2016
#     Thu Oct 20 11:45:11 PDT 2016
#     Thu Oct 20 11:45:12 PDT 2016
#     Thu Oct 20 11:45:13 PDT 2016
#     Thu Oct 20 11:45:14 PDT 2016
#
