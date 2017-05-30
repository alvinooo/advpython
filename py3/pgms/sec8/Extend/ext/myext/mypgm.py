#!/usr/bin/env python3
# mypgm.py - myext extension module
import myext

print(myext.greeting())
val = myext.mult(2.5, 3.5)
print(val)

mystr = "radar"
(mystr, num) = myext.replace(mystr, old="r", new="m")
print("number of changes = %s" %num)
print(mystr)

point1 = [5, 10]
point2 = [2, 6]
print("%g" %myext.slope(point1, point2))

(answer, remainder) = myext.divide(9, 4)
print("answer = %d" %answer)
print("remainder = %d" %remainder)

###########################################
#
#     $ mypgm.py
#     C: initializing myext module
#     hello there, from C
#     20
#     8.75
#     number of changes = 2
#     madam
#     1.33333
#     Traceback (most recent call last):
#       File "./mypgm.py", line 18, in <module>
#         (answer, remainder) = myext.divide(9, 4)
#     NotImplementedError: divide() not implemented.
#
