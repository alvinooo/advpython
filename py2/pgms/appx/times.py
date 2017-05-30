#!/usr/bin/env python
# times.py - time module
from time import sleep, time, ctime
from time import localtime, strftime

print ctime()

now = localtime(time())
print now

print "Month = %d" %now.tm_mon
print "Day = %d" %now.tm_mday
print "Year = %d" %now.tm_year

d1 = strftime("%a %b %d %H:%M:%S %Y", now)
print d1

print "sleeping for 3.5 secs..."
sleep(3.5)
print "done"

###############################################
#
#    $ times.py
#    Fri Jul  8 18:28:11 2016
#    time.struct_time(tm_year=2016, tm_mon=7, tm_mday=8, 
#    tm_hour=18, tm_min=28, tm_sec=11, tm_wday=4, 
#    tm_yday=190, tm_isdst=1)
#    Month = 7
#    Day = 8
#    Year = 2016
#    Fri Jul 08 18:28:11 2016
#    sleeping for 3.5 secs...
#    done
#
