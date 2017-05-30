# Clock.py - Clock module
from threading import *
from time import *
from logging import *
basicConfig(level=ERROR, format="(%(threadName)s) %(message)s",)

class Clock(Thread):
    def __init__(self, interval):
        super().__init__()
        self.__nap = interval
        self.__stop = False

    def cancel(self):
        debug("Clock stopped")
        self.__stop = True

    def run(self):
        debug("Clock started")
        while (True):
            if self.__stop: 
                break
            print(ctime())
            sleep(self.__nap)

