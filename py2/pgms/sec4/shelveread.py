#!/usr/bin/env python
# shelveread.py - shelve reads
import shelve

media = {}                             # dictionary
sdb = shelve.open("dbshelve", "r")
print "%s entries in shelf" %len(sdb)  # number of entries
for (key, value) in sdb.items():
    media[key] = value
print "keys:", media.keys()            # keys in shelf
print "values:", [sdb[key] for key in sdb.keys()]
sdb.close()

#################################################
#
#    $ shelveread.py
#    2 entries in shelf
#    keys: ['music', 'film']
#    values: [{'jazz': 'miles davis', 'pop': 'billy joel', 'rock': 'sting'},
#    {'color': 'fantasia', 'black & white': 'pyscho'}]
#
