#!/usr/bin/env python
# coroutine3.py - coroutine send and receive
from functools import wraps

def coroutine(func):
    @wraps(func)
    def begin(*args, **kwargs):
        funcref = func(*args, **kwargs)
        funcref.next()
        return funcref
    return begin

@coroutine
def mysplit(delimiter=None):
    result = None
    while True:
        line = yield result
        result = line.lower().split(delimiter)

s = mysplit()
rec = s.send("ONE TWO THREE")
print rec

s = mysplit(":")
rec = s.send("BOB:45:ACCOUNTING")
print rec

s = mysplit(",")
rec = s.send("Test10,TEST20")
print rec

#####################################

#     $ coroutine3.py
#     ['one', 'two', 'three']
#     ['bob', '45', 'accounting']
#     ['test10', 'test20']
#      
