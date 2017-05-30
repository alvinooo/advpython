# MyTask.py - MyTask class
import sqlite3
from TaskThread import Task
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

class MyTask(Task):
    def __init__(self, name):
        super().__init__(name)
        self.__file = open(name, "w")
        debug("%s file opened" %name)

    def close(self):
        debug("%s file closed" %self.name)
        self.__file.close()

    def execute(self, sql):
        debug("running sql: '%s'" %sql)
        self.__file.write("sql: %s\n" %sql)
        try:
            conn = sqlite3.connect("BookCatalog.db")
            conn.execute(sql)
            conn.commit()
            conn.close()
        except sqlite3.DatabaseError as ex:
            output = "SQLError - %s" %ex

