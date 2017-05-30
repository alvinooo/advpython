#!/usr/bin/env python
# rlocks.py - reentrant thread locks
from Pair import Pair
from threading import *
from time import sleep
from random import random
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def myThread(pair, val):
    pause = random()
    sleep(pause)
    pair.addBoth(val)

pair = Pair(10, 20)
debug("Pair = %s", pair)

for num in range(2, 4):
    thread = Thread(target=myThread, args=(pair, num+2))
    thread.start()

debug("Waiting for pair threads")
mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        thread.join()
debug("Pair = %s", pair)

#################################################
#
#     $ rlocks.py
#     (MainThread) Pair = 10 20
#     (MainThread) Waiting for pair threads
#     (Thread-2) Add to pair by 5
#     (Thread-2) Add to left by 5
#     (Thread-2) Add to right by 5
#     (Thread-1) Add to pair by 4
#     (Thread-1) Add to left by 4
#     (Thread-1) Add to right by 4
#     (MainThread) Pair = 19 29
#
