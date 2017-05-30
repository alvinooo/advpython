#!/usr/bin/env python3
# dbmdelete.py - delete dbm persistence
import dbm

db = dbm.open("media", 'w')    # open dbm for write
print("%s entries in dbm" %len(db))
print("keys:", list(db.keys()))
print("values:", [db[key] for key in db.keys()])
if "pop" in db:                # check for key
    del db["pop"]              # delete from dbm

print("%s entries in dbm" %len(db))   # number of entries
print("keys:", list(db.keys()))       # keys in dbm
print("values:", [db[key] for key in db.keys()])
db.close()                            # close dbm

#################################################
#
#    $ dbmdelete.py
#    6 entries in dbm
#    keys: [b'black & white', b'color', b'drama', b'jazz', b'pop', b'rock']
#    values: [b'pyscho', b'fantasia', b'law & order', b'miles davis', 
#    b'billy joel', b'sting']
#    5 entries in dbm
#    keys: [b'black & white', b'color', b'drama', b'jazz', b'rock']
#    values: [b'pyscho', b'fantasia', b'law & order', b'miles davis', b'sting']
#    
