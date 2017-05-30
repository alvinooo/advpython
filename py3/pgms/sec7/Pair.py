# Pair.py - Pair module
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class Pair():
    def __init__(self, left=0, right=0):
        self._left = left
        self._right = right
        self.__lock = RLock()    # reentrant lock

    def addLeft(self, val):
        with self.__lock:
            debug("Add to left by %d" %val)
            self._left += val

    def addRight(self, val):
        with self.__lock:
            debug("Add to right by %d" %val)
            self._right += val

    def addBoth(self, val):
        with self.__lock:
            debug("Add to pair by %d" %val)
            self.addLeft(val)
            self.addRight(val)

    def __str__(self):
        return "%d %d" %(self._left, self._right)

