#!/usr/bin/env python3
# serial.py - no threads or processes
from time import time

def isPerfect(number):
    perfect = 0
    for n in range(1, number):
        if (number % n == 0):
            perfect += n
    return perfect == number

numbers = [28, 496, 8128, 55204386, 33550336]
print(numbers)

start = time()
results = list(map(isPerfect, numbers))
print(results)
end = time()
print("Took %g seconds" %(end - start))

#####################################
#
#     $ serial.py
#     [28, 496, 8128, 55204386, 33550336]
#     [True, True, True, False, True]
#     Took 5.46959 seconds
#      
