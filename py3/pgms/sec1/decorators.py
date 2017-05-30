#!/usr/bin/env python3
# decorators.py - multiple decorators
import math

def nonNegative(func): 
    def checker(arg):
        arg = arg if arg >= 0 else -arg
        return func(arg)
    return checker

def nonZero(func): 
    def checker(arg):
        arg = 1 if arg == 0 else arg
        return func(arg)
    return checker

@nonNegative
@nonZero
def circum(radius):
    return 2 * math.pi * radius

# implemented as: circum = nonNegative(nonZero(circum))

c1 = circum(10)
print(c1)
c2 = circum(-10)
print(c2)
c3 = circum(0)
print(c3)

#####################################
#
#     $ decorators.py
#     62.8318530718
#     62.8318530718
#     6.28318530718
#      
