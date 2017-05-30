#!/usr/bin/env python
# semaphores.py - semaphores with thread pool
from ThreadPool import ThreadPool
from threading import *
from time import sleep 
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def myThread(sem, pool):
    debug("Waiting to join the pool")
    with sem:
        name = current_thread().name
        pool.makeActive(name)
        sleep(.5)           # access resource
        pool.makeInactive(name)

pool = ThreadPool()
sem = Semaphore(3)
for num in range(6):
    thread = Thread(target=myThread, args=(sem, pool))
    thread.start()

#################################################
#
#     $ semaphores.py
#     (Thread-1) Waiting to join the pool
#     (Thread-1) Active: ['Thread-1']
#     (Thread-2) Waiting to join the pool
#     (Thread-2) Active: ['Thread-1', 'Thread-2']
#     (Thread-3) Waiting to join the pool
#     (Thread-3) Active: ['Thread-1', 'Thread-2', 'Thread-3']
#     (Thread-4) Waiting to join the pool
#     (Thread-5) Waiting to join the pool
#     (Thread-6) Waiting to join the pool
#     (Thread-1) Inactive: ['Thread-2', 'Thread-3']
#     (Thread-2) Inactive: ['Thread-3']
#     (Thread-4) Active: ['Thread-3', 'Thread-4']
#     (Thread-5) Active: ['Thread-3', 'Thread-4', 'Thread-5']
#     (Thread-3) Inactive: ['Thread-4', 'Thread-5']
#     (Thread-6) Active: ['Thread-4', 'Thread-5', 'Thread-6']
#     (Thread-4) Inactive: ['Thread-5', 'Thread-6']
#     (Thread-5) Inactive: ['Thread-6']
#     (Thread-6) Inactive: []
#     
