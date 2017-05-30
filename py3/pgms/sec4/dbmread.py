#!/usr/bin/env python3
# dbmread.py - read dbm persistence
import dbm

db = dbm.open("media", 'r')          # open dbm for read
print("%s entries in dbm" %len(db))
print("keys:", list(db.keys()))      # keys in dbm
print("values:", [db[key] for key in db.keys()])
db.close()                           # close dbm

#################################################
#
#    $ dbmread.py
#    5 entries in dbm
#    keys: [b'black & white', b'color', b'jazz', b'pop', b'rock']
#    values: [b'pyscho', b'fantasia', b'miles davis', 
#    b'billy joel', b'sting']
# 
