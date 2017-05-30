# MyData.py - MyData module
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyData(object):
    def __init__(self, data):
        self.__data = data
        self.__read_sem = Semaphore(0)
        self.__write_sem = Semaphore(1)

    def readData(self):
        self.__read_sem.acquire()
        data = self.__data
        self.__write_sem.release()
        return data

    def writeData(self, data):
        self.__write_sem.acquire()
        self.__data = data
        self.__read_sem.release()

