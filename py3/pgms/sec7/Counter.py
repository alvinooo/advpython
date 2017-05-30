# Counter.py - Counter class, acquire/release
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class Counter():
    def __init__(self, start=0):
        self.__lock = Lock()
        self._value = start

    def incr(self):
        self.__lock.acquire()
        try:
            debug("Acquired lock")
            self._value += 1
        finally:
            self.__lock.release()
            debug("Released lock")
#
