# Consumer.py - Consumer module
from multiprocessing import Process
from logging import *
basicConfig(level=DEBUG, format="(%(processName)s) %(message)s",)

class Consumer(Process):
    def __init__(self, taskq, resultq):
        super().__init__()
        self.__taskq = taskq
        self.__resultq = resultq

    def run(self):
        while True:
            task = self.__taskq.get()
            if task is None:
                debug("Exiting")
                self.__taskq.task_done()
                break
            debug("process %d: %s" %(self.pid, task))
            result = task()     # invokes Task.__call__(task)
            self.__taskq.task_done()
            self.__resultq.put(result)

