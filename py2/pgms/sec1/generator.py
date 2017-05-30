#!/usr/bin/env python
# generator.py - generators and yield

def countDown(num):
    print "Counting down from %d" %num
    while num >= 0:
        yield num      # return and stop
        num -= 1

counter = countDown(5)
print counter.next()
print counter.next()

for n in countDown(10):
    print n,
print

total = sum(countDown(5))
print total

#####################################
#
#     $ generator.py
#     Counting down from 5
#     5
#     4
#     Counting down from 10
#     10 9 8 7 6 5 4 3 2 1 0
#     Counting down from 5
#     15
#
