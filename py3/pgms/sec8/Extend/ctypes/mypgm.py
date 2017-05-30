#!/usr/bin/env python3
# mypgm.py - ctypes demo
import myclib
from myclib import Point

myclib.greeting(b'bob')
print(myclib.add(2, 3))
print(myclib.mult(2.5, 3.5))

(answer, remainder) = myclib.divide(9, 4)
print("answer = %d" %answer)
print("remainder = %d" %remainder)
    
mylist = [1,2,3,4,5,6,7,8,9,10]
print(myclib.avg(mylist))
    
mytuple = (5,6,7,8,9,10)
print(myclib.avg(mytuple))

mystr = b'radar'
(mystr, num) = myclib.replace(mystr, b'r', b'm')
print("Number of changes = %s" %num)
print(mystr.decode("ascii"))

p1 = Point(5, 10)
p2 = Point(2, 6)
print("%g" %myclib.slope(p1, p2))

############################################
#
#     $ mypgm.py
#     hello there, bob
#     5
#     8.75
#     answer = 2
#     remainder = 1
#     5.5
#     7.5
#     Number of changes = 2
#     madam
#     1.33333
#
