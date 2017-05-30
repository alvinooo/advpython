#!/usr/bin/env python
# rwlocks.py - read-write locking
from RWLock import RWLock
from threading import *
from time import sleep
from random import random
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def writer(mylock):
    mylock.acquire_write()
    debug("start writing to resource")
    sleep(random())
    debug("done writing to resource")
    mylock.release_write()

def reader(mylock):
    mylock.acquire_read()
    debug("start reading from resource")
    sleep(random())
    debug("done reading from resource")
    mylock.release_read()
            
rwlock = RWLock()
Thread(target=reader, name="Reader-1", args=(rwlock,)).start()
Thread(target=writer, name="Writer-1", args=(rwlock,)).start()
Thread(target=reader, name="Reader-2", args=(rwlock,)).start()
Thread(target=reader, name="Reader-3", args=(rwlock,)).start()
#Thread(target=writer, name="Writer-2", args=(rwlock,)).start()

#################################################
#
#     $ rwlocks.py
#     (Reader-1) start reading from resource
#     (Writer-1) write is waiting
#     (Reader-2) start reading from resource
#     (Reader-3) start reading from resource
#     (Reader-3) done reading from resource
#     (Reader-1) done reading from resource
#     (Reader-2) done reading from resource
#     (Reader-2) ok to write now
#     (Writer-1) start writing to resource
#     (Writer-1) done writing to resource
#     
