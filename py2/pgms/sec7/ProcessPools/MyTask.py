# MyTask.py - MyTask class
from TaskThread import Task
from logging import *
basicConfig(level=ERROR, format="(%(threadName)s) %(message)s",)

def isPerfect(number):
    perfect = 0
    for n in range(1, number):
        if (number % n == 0):
            perfect += n
    return perfect == number

class MyTask(Task):
    def __init__(self, name=None):
        super(MyTask, self).__init__(name)

    def close(self): pass

    def execute(self, num):
        debug("finding result for %s" %num)
        self.name.append(isPerfect(num))

