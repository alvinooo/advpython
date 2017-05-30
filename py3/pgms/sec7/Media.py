# Media.py - Media module
from datetime import datetime
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class Media(object):
    def __init__(self, title):
        self._title = title
        self.__videoReady = Event()
        self.__audioReady = Event()

    def playVideo(self):
        self.__videoReady.set()
        self.__audioReady.wait()
        debug("playing %s video at %d" 
            %(self._title, datetime.now().microsecond))

    def playAudio(self):
        self.__audioReady.set()
        self.__videoReady.wait()
        debug("playing %s audio at %d" 
            %(self._title, datetime.now().microsecond))

