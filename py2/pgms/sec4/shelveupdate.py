#!/usr/bin/env python
# shelveupdate.py - shelve updates
import shelve

sdb = shelve.open("dbshelve", writeback=True)
sdb["music"]["rock"] = "eagles"

print "%s entries in shelf" %len(sdb)    # number of entries
print "keys:", sdb.keys()                # keys in shelf
print "values:", [sdb[key] for key in sdb.keys()]
sdb.close()

#################################################
#
#    $ shelveupdate.py
#    2 entries in shelf
#    keys: ['film', 'music']
#    values: [{'color': 'fantasia', 'black & white': 'pyscho'}, 
#    {'jazz': 'miles davis', 'pop': 'billy joel', 'rock': 'eagles'}]
#
