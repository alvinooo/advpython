#!/usr/bin/env python
# dbmdelete.py - delete dbm persistence
import dumbdbm as dbm

db = dbm.open("media", 'w')          # open dbm for write
print "%s entries in dbm" %len(db)
print "keys:", db.keys()             # keys in dbm
print "values:", [db[key] for key in db.keys()]
if db.has_key("pop"):                # check for key
    del db["pop"]                    # delete from dbm

print "%s entries in dbm" %len(db)   # number of entries
print "keys:", db.keys()             # keys in dbm
print "values:", [db[key] for key in db.keys()]
db.close()                           # close dbm

#################################################
#
#    $ dbmdelete.py
#    6 entries in dbm
#    keys: ['color', 'jazz', 'pop', 'drama', 'rock', 'black & white']
#    values: ['fantasia', 'miles davis', 'billy joel', 'law & order',
#    'sting', 'pyscho']
#    5 entries in dbm
#    keys: ['color', 'jazz', 'drama', 'rock', 'black & white']
#    values: ['fantasia', 'miles davis', 'law & order', 'sting', 'pyscho']
#    
