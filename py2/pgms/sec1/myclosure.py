#!/usr/bin/env python
# myclosure.py - counter closure function

def countDown(num):
    countDown.num = num
    def next():
        countDown.num -= 1
        return countDown.num
    return next

counter = countDown(10000000)
while True:
    number = counter()
    if not number: break

#####################################
#
#     $ time myclosure.py
#     real:   0m2.736s 
#     user:   0m2.584s 
#     sys:    0m0.024s 
#
