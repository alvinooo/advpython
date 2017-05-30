#!/usr/bin/env python3
# dbmwrite.py - write dbm persistence
import dbm

media = { "jazz" : "miles davis",
          "rock" : "sting",
          "pop"  : "billy joel",
          "color" : "fantasia",
          "black & white" : "pyscho"
        }

db = dbm.open("media", 'n')          # open new dbm
for (key, value) in list(media.items()):
    db[key] = value                  # add to dbm

print("%s entries in dbm" %len(db))  # number of entries
print("keys:", list(db.keys()))      # keys in dbm
print("values:", [db[key] for key in db.keys()])
db.close()                           # close dbm

#################################################
#
#    $ dbmwrite.py
#    5 entries in dbm
#    keys: [b'black & white', b'color', b'jazz', b'pop', b'rock']
#    values: [b'pyscho', b'fantasia', b'miles davis', 
#    b'billy joel', b'sting']
# 
