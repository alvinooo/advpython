# RWLock.py - RWLock module
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class RWLock:
    def __init__(self):
        self.__cond = Condition()
        self.__readers = 0

    def acquire_read(self):
        with self.__cond:
            self.__readers += 1 

    def release_read(self): 
        with self.__cond:
            self.__readers -= 1
            if not self.__readers: 
                debug("ok to write now")
                self.__cond.notifyAll()

    def acquire_write(self): 
        self.__cond.acquire() 
        while self.__readers > 0:
            debug("write is waiting")
            self.__cond.wait()

    def release_write(self):
        self.__cond.release()

