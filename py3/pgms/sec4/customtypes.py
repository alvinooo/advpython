#!/usr/bin/env python3
# customtypes.py - custom types
import sqlite3, pickle
from Person import Person

def myadapter(obj):
    print("myadapter:", type(obj))
    return pickle.dumps(obj)

def myconverter(data):
    print("myconverter:", type(data))
    return pickle.loads(data)

sqlite3.register_adapter(Person, myadapter)
sqlite3.register_converter("Person", myconverter)

conn = sqlite3.connect("Person.db",
    detect_types = sqlite3.PARSE_COLNAMES)
cursor = conn.execute("""
    CREATE TABLE IF NOT EXISTS objects (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        data TEXT
    )""") 

objs = ((Person("Bob", 45),), (Person("Sue", 33),))
conn.executemany("""INSERT INTO objects 
    (data) VALUES (?)""", objs)

cursor = conn.execute("SELECT id, data as 'pickle[Person]' from objects")
for (id, obj) in cursor:
    print(id, obj)
conn.close()

#################################################
#
#    $ customtypes.py
#    myadapter: <class 'Person.Person'>
#    myadapter: <class 'Person.Person'>
#    myconverter: <class 'bytes'>
#    myconverter: <class 'bytes'>
#    1 Person: Bob 45
#    2 Person: Sue 33
#    
