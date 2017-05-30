#!/usr/bin/env python3
# timedeltas.py - timedelta objects in datetime module
from datetime import timedelta, datetime

td1 = timedelta(days=2, hours=18)
td2 = timedelta(hours=8.5)
td3 = td1 + td2
days = td3.days
hours = td3.seconds / float(3600)
hoursahead = td3.total_seconds() / 3600
print(days, hours, hoursahead)

dt1 = datetime(2016, 2, 25)
dt2 = datetime(2016, 3, 6)
td4 = dt2 - dt1
print(td4.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

###############################################
#
#    $ timedeltas.py
#    3 2.5 74.5
#    10
#    2016-07-09 14:34:36.785123
#    2016-07-09 14:44:36.785123
# 
