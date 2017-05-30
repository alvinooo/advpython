#!/usr/bin/env python3
# dtimes.py - time objects in datetime module
from datetime import time

time1 = time(10, 20, 30)
print(time1)
print(time1.hour, time1.minute, time1.second)

time2 = time1.replace(hour=20, minute=45)
print(time2)

timestring = time2.strftime("%H:%M%P")
print("The time is %s" %timestring)

if time2 > time(18, 0, 0):
    print("evening time")

###############################################
#
#    $ dtimes.py
#    10:20:30
#    10 20 30
#    20:45:30
#    The time is 20:45pm
#    evening time
# 
