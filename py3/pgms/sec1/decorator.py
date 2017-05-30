#!/usr/bin/env python3
# decorator.py - decorator function
import math

def nonNegative(func): 
    def checker(arg):
        arg = arg if arg >= 0 else -arg
        return func(arg)
    return checker

@nonNegative
def circum(radius):
    return 2 * math.pi * radius

# implemented as: circum = nonNegative(circum)

c1 = circum(10)
print(c1)
c2 = circum(-10)
print(c2)

#####################################
#
#     $ decorator.py
#     62.8318530718
#     62.8318530718
#      
