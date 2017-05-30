#!/usr/bin/env python3
# threads.py - compute with threads
from MyTask import MyTask
from TaskThread import *
from time import time

numbers = [28, 496, 8128, 55204386, 33550336]
print(numbers)

start = time()
results = []
mytask = MyTask(results)
task = TaskThread(mytask)
task.start()
for num in numbers:
    task.send(num)
task.close()
end = time()
print(results)
print("Took %g seconds" %(end - start))

#################################################
#
#     $ threads.py
#     [28, 496, 8128, 55204386, 33550336]
#     [True, True, True, False, True]
#     Took 5.82028 seconds
#
