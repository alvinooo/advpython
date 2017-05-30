#!/usr/bin/env python
# dbmwrite.py - write dbm persistence
import dumbdbm as dbm

media = { "jazz" : "miles davis",
          "rock" : "sting",
          "pop"  : "billy joel",
          "color" : "fantasia",
          "black & white" : "pyscho"
        }

db = dbm.open("media", 'n')         # open new dbm
for (key, value) in media.items():
    db[key] = value                 # add to dbm

print "%s entries in dbm" %len(db)  # number of entries
print "keys:", db.keys()            # keys in dbm
print "values:", [db[key] for key in db.keys()]
db.close()                          # close dbm

#################################################
#
#    $ dbmwrite.py
#    5 entries in dbm
#    keys: ['color', 'jazz', 'black & white', 'pop', 'rock']
#    values: ['fantasia', 'miles davis', 'pyscho', 'billy joel', 'sting']
# 
