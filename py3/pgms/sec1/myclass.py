#!/usr/bin/env python3
# myclass.py - counter class

class CountDown:
    def __init__(self, num):
        self.num = num
    def next(self):
        self.num -= 1
        return self.num

counter = CountDown(10000000)
while True:
    number = counter.next()
    if not number: break

#####################################
#
#     $ time myclass.py
#     real:   0m2.875s 
#     user:   0m2.740s 
#     sys:    0m0.016s 
#
