# ThreadPool.py - thread pool
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class ThreadPool(object):
    def __init__(self):
        self.__active = []
        self.__lock = Lock()
    def makeActive(self, name):
        with self.__lock:
            self.__active.append(name)
            debug("Active: %s", self.__active)
    def makeInactive(self, name):
        with self.__lock:
            self.__active.remove(name)
            debug("Inactive: %s", self.__active)
