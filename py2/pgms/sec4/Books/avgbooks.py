#!/usr/bin/env python
# avgbooks.py - average book copies
import sqlite3

class Average(object):
    def __init__(self):
        self.__total = 0.0
        self.__count = 0
    def step(self, value):
        self.__total += value
        self.__count += 1
    def finalize(self):
        return self.__total / self.__count

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("SELECT title, copies FROM BookCatalog") 
for (title, copies) in cursor:
    print title, copies

conn.create_aggregate("avg", 1, Average)
cursor = conn.execute("SELECT avg(copies) FROM BookCatalog") 
print "avg number of books = ", cursor.fetchone()[0]
conn.close()

#################################################
#
#    $ avgbooks.py
#    Les Miserables 1
#    Jurassic Park 3
#    The Firm 2
#    Tales From Margaritaville 1
#    avg number of books =  1.75
# 
