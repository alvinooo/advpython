#!/usr/bin/env python3
# dbmupdate.py - update dbm persistence
import dbm

db = dbm.open("media", 'w')          # open dbm for read,write
print("%s entries in dbm" %len(db))
print("keys:", list(db.keys()))      # keys in dbm
print("values:", [db[key] for key in db.keys()])

db["drama"] = "law & order"          # add to dbm
print("%s entries in dbm" %len(db))
db.close()                           # close dbm

#################################################
#
#    $ dbmupdate.py
#    5 entries in dbm
#    keys: [b'black & white', b'color', b'jazz', b'pop', b'rock']
#    values: [b'pyscho', b'fantasia', b'miles davis', 
#    b'billy joel', b'sting']
#    6 entries in dbm
#
