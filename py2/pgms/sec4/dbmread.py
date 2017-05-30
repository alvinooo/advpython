#!/usr/bin/env python
# dbmread.py - read dbm persistence
import dumbdbm as dbm

db = dbm.open("media", 'r')          # open dbm for read
print "%s entries in dbm" %len(db)
print "keys:", db.keys()             # keys in dbm
print "values:", [db[key] for key in db.keys()]
db.close()                           # close dbm

#################################################
#
#    $ dbmread.py
#    5 entries in dbm
#    keys: ['color', 'jazz', 'black & white', 'pop', 'rock']
#    values: ['fantasia', 'miles davis', 'pyscho', 'billy joel', 'sting']
# 
