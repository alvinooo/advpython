#!/usr/bin/env python3
# myclosure.py - counter closure function

def countDown(num):
    def next():
        nonlocal num
        num -= 1
        return num
    return next

counter = countDown(10000000)
while True:
    number = counter()
    if not number: break

#####################################
#
#     $ time myclosure.py
#     real:   0m1.745s 
#     user:   0m1.612s 
#     sys:    0m0.028s 
#
