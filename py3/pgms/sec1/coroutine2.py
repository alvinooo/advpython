#!/usr/bin/env python3
# coroutine2.py - coroutine decorator
from functools import wraps

def coroutine(func):
    @wraps(func)
    def begin(*args, **kwargs):
        funcref = func(*args, **kwargs)
        next(funcref)
        return funcref
    return begin

@coroutine
def receiver():
    while True:
        msg = yield
        print(msg)

rec = receiver()
rec.send("message 1")
rec.send("message 2")
rec.close()

#####################################

#     $ coroutine2.py
#     message 1
#     message 2
#      
