# TaskThread.py - TaskThread module
from threading import *
from queue import Queue
from abc import *
from logging import *
basicConfig(level=ERROR, format="(%(threadName)s) %(message)s",)

class Task(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @property 
    def name(self): return self.__name

    @abstractmethod
    def execute(self, data): pass

    @abstractmethod
    def close(self): pass

class TaskThread(Thread):
    def __init__(self, task):
        super(TaskThread, self).__init__(name=task.name)
        self.__queue = Queue()           # task queue
        self.__task = task               # task to run

    def send(self, data):
        debug("put '%s' in queue" %data)
        self.__queue.put(data)           # put data in queue

    def close(self):
        debug("closing queue")
        self.__queue.put(None)           # finished sentinel
        self.__queue.join()              # wait for empty queue
        debug("closing task")
        self.__task.close()

    def run(self):
        while True:
            data = self.__queue.get()    # data from queue
            if data is None:             # check sentinel
                break                    # thread finished
            self.__task.execute(data)    # execute task
            self.__queue.task_done()     # done with task
        self.__queue.task_done()         # done with all tasks

