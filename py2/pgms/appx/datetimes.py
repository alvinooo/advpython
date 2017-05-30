#!/usr/bin/env python
# datetimes.py - datetime objects in datetime module
from datetime import datetime, date, time

dtime1 = datetime(2016, 2, 14, 8, 25, 40)
print dtime1
date1 = dtime1.date()
time1 = dtime1.time()
print date1, time1

dtime2 = dtime1.replace(month=5, hour=11)
print dtime2

date1 = date(2015, 12, 20)
time1 = time(9, 15, 0)
dtime3 = datetime.combine(date1, time1)
print dtime3

dtime4 = datetime.strptime("3/10/15 15:30", "%m/%d/%y %H:%M")
print dtime4

timestring = datetime.now().strftime("%H:%M%P")
print "The time is now %s" %timestring

###############################################
#
#    $ datetimes.py
#    2016-02-14 08:25:40
#    2016-02-14 08:25:40
#    2016-05-14 11:25:40
#    2015-12-20 09:15:00
#    2015-03-10 15:30:00
#    The time is now 13:31pm
# 
