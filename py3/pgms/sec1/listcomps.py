#!/usr/bin/env python3
# listcomps.py - list comprehensions
import math

# celsius to fahrenheit conversion
ctemps = [22.4, 32.5, -40]
ftemps = [(9.0 / 5.0) * c + 32 for c in ctemps]
print(ftemps)

# associate negative values
L1 = [-3, 8, -5]
L2 = [-4, 10, -6]
L3 = [(a, b) for a in L1 if a < 0 for b in L2 if b < 0]
print(L3)

# find hypotenuse
nums = [(3, 4), (6, 8), (9, 12)] 
hypots = [math.sqrt(x*x + y*y) for (x,y) in nums]
print(hypots)

#####################################
#
#     $ listcomps.py
#     [72.32, 90.5, -40.0]
#     [(-3, -4), (-3, -6), (-5, -4), (-5, -6)]
#     [5.0, 10.0, 15.0]
#      
