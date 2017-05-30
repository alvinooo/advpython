#!/usr/bin/env python3
# dates.py - date objects in datetime module
from datetime import date

date1 = date.today()
print(date1.ctime())

date2 = date(2016, 4, 15)
print(date2.ctime())
print(date2.month, date2.day, date2.year)

date3 = date2.replace(month=6)
print(date3.ctime())

datestring = date3.strftime("%a %d %b %Y")
print(datestring)

today = date.today().timetuple()
print("today is day %d of the year" %today[7])

###############################################
#
#    $ dates.py
#    Sat Jul  9 00:00:00 2016
#    Fri Apr 15 00:00:00 2016
#    4 15 2016
#    Wed Jun 15 00:00:00 2016
#    Wed 15 Jun 2016
#    today is day 191 of the year
# 
