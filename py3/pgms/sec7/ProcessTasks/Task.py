# Task.py - Task module
import urllib.request, urllib.error, urllib.parse, re
from logging import *
basicConfig(level=DEBUG, format="(%(processName)s) %(message)s",)

class Task(object):
    def __init__(self, url, nlinks=None):
        self.__url = url
        self.__nlinks = nlinks

    def __call__(self):
        website = urllib.request.urlopen("http://%s" %self.__url)
        html = website.read()
        regex = '"((http|ftp)s?://.*?)"'.encode("ascii")
        links = re.findall(regex, html)
        if self.__nlinks is None: 
            self.__nlinks = len(links)
        debug("found %d links for %s"  
            %(self.__nlinks, self.__url))
        return [link[0] for link in links[:self.__nlinks]] 

    def __str__(self):
        return "%s" %self.__url
