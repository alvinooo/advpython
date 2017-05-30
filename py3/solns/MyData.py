# MyData.py - MyData module
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyData(object):
    def __init__(self, data):
        self.__data = data
        self.__reading = Semaphore(0)
        self.__writing = Semaphore(1)

    def readData(self):
        try:
            self.__reading.acquire()
            return self.__data
        finally:
            self.__writing.release()

    def writeData(self, data):
        try:
            self.__writing.acquire()
            self.__data = data
        finally:
            self.__reading.release()

