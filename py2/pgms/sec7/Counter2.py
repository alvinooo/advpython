# Counter2.py - Counter class, with statment
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class Counter():
    def __init__(self, start=0):
        self.__lock = Lock()
        self._value = start

    def incr(self):
        with self.__lock:
            debug("Acquired lock")
            self._value += 1
        debug("Released lock")
