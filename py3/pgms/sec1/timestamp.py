#!/usr/bin/env python3
# timestamp.py - closure
from time import time, sleep

def timestamp():
    start = time()
    def duration():
        return time() - start
    return duration

def doSomeThing(n):
    sleep(n)

then = timestamp()
doSomeThing(2)
print("%1.0f seconds since then" %then())

now = timestamp()
doSomeThing(3)
print("%1.0f seconds since now" %now())
print("%1.0f seconds since then" %then())

#####################################
#
#     $ timestamp.py
#     2 seconds since then
#     3 seconds since now
#     5 seconds since then
#      
