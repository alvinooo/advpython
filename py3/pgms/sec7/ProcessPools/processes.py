#!/usr/bin/env python3
# processes.py - compute with processes
from time import time
from multiprocessing import *

def isPerfect(number):
    perfect = 0
    for n in range(1, number):
        if (number % n == 0):
            perfect += n
    return perfect == number

if __name__ == "__main__":
    numCores = cpu_count()
    print("Number of cores = %d" %numCores)

    numbers = [28, 496, 8128, 55204386, 33550336]
    print(numbers)

    start = time()
    pool = Pool(processes=numCores)
    results = pool.map(isPerfect, numbers)
    pool.close(); pool.join()
    print(results)
    end = time()
    print("Took %g seconds" %(end - start))

#####################################
#
#     $ processes.py
#     Number of cores = 1
#     [28, 496, 8128, 55204386, 33550336]
#     [True, True, True, False, True]
#     Took 5.53461 seconds
#      
