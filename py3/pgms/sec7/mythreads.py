#!/usr/bin/env python3
# mythreads.py - creating threads, debugging
from threading import *
from random import randint
from time import sleep
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def myThread():
    pause = randint(1, 5)
    debug("sleeping %s" %pause)
    sleep(pause)
    debug("wakeup")

for i in range(3):
    mythread = Thread(target=myThread)
    mythread.start()

mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        debug("joining %s" %thread.name)
        thread.join()
debug("done")

##################################################
#
#     $ mythreads.py
#     (Thread-1) sleeping 2
#     (Thread-2) sleeping 1
#     (MainThread) joining Thread-1
#     (Thread-3) sleeping 3
#     (Thread-2) wakeup
#     (Thread-1) wakeup
#     (MainThread) joining Thread-2
#     (MainThread) joining Thread-3
#     (Thread-3) wakeup
#     (MainThread) done
#
