#!/usr/bin/env python
# dbmupdate.py - update dbm persistence
import dumbdbm as dbm

db = dbm.open("media", 'w')          # open dbm for read,write
print "%s entries in dbm" %len(db)
print "keys:", db.keys()             # keys in dbm
print "values:", [db[key] for key in db.keys()]

db["drama"] = "law & order"          # add to dbm
print "%s entries in dbm" %len(db)
db.close()                           # close dbm

#################################################
#
#    $ dbmupdate.py
#    5 entries in dbm
#    keys: ['color', 'jazz', 'black & white', 'pop', 'rock']
#    values: ['fantasia', 'miles davis', 'pyscho', 'billy joel', 'sting']
#    6 entries in dbm
#
