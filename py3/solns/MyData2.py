# MyData2.py - MyData module, with statement do NOT work ...
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyData(object):
    def __init__(self, data):
        self.__data = data
        self.__reading = Semaphore(0)
        self.__writing = Semaphore(1)

    def readData(self):
        with self.__reading:
            return self.__data
        self.__writing.release()

    def writeData(self, data):
        with self.__writing:
            self.__data = data
        self.__reading.release()

