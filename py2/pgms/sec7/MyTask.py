# MyTask.py - MyTask class
from TaskThread import Task
import urllib2, re
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyTask(Task):
    def __init__(self, name):
        super(MyTask, self).__init__(name)
        self.__file = open(name, "w")
        debug("%s file opened" %name)

    def close(self):
        debug("%s file closed" %self.name)
        self.__file.close()

    def execute(self, url):
        debug("finding links for %s" %url)
        website = urllib2.urlopen("http://%s" %url)
        html = website.read()
        regex = '"((http|ftp)s?://.*?)"'
        links = re.findall(regex, html)
        self.__file.write("Links for %s:\n" %url)
        for link in links:
            self.__file.write("%s\n" %link[0])

