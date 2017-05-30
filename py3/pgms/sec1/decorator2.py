#!/usr/bin/env python3
# decorator2.py - decorator function
import math
from functools import wraps
from time import time

def timeThis(func): 
    @wraps(func)
    def timeElapsed(*args, **kwargs):
        begin = time()
        result = func(*args, **kwargs)
        end = time()
        print(func.__name__, end-begin) 
        return result
    return timeElapsed

@timeThis
def isPerfect(number):
    perfect = 0
    for n in range(1, number):
        if (number % n == 0):
            perfect += n
    return perfect == number
# implemented as: isPerfect = timeThis(isPerfect)

print(isPerfect(33550336))
print(isPerfect.__name__)

#####################################
#
#     $ decorator2.py
#     isPerfect 2.17572903633
#     True
#     isPerfect
#      
