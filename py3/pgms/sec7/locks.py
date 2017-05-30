#!/usr/bin/env python3
# locks.py - thread locks
from Counter import Counter
from threading import *
from time import sleep
from random import random
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def myThread(counter):
    for num in range(2):
        pause = random()
        sleep(pause)
        counter.incr()

counter = Counter()
debug("Counter = %d", counter._value)

for num in range(2):
    thread = Thread(target=myThread, args=(counter,))
    thread.start()

debug("Waiting for counter threads")
mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        thread.join()
debug("Counter = %d", counter._value)

#################################################
#
#     $ locks.py
#     (MainThread) Counter = 0
#     (MainThread) Waiting for counter threads
#     (Thread-2) Acquired lock
#     (Thread-2) Released lock
#     (Thread-1) Acquired lock
#     (Thread-1) Released lock
#     (Thread-2) Acquired lock
#     (Thread-2) Released lock
#     (Thread-1) Acquired lock
#     (Thread-1) Released lock
#     (MainThread) Counter = 4
#
