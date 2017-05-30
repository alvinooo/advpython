# MyData.py - MyData module
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyData(object):
    def __init__(self, data):
        self.__data = data

    def readData(self):
        return self.__data

    def writeData(self, data):
        self.__data = data

