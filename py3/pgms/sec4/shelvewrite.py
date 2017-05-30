#!/usr/bin/env python3
# shelvewrite.py - shelve writes
import shelve

media = { "music" : 
            { "jazz" : "miles davis",
              "rock" : "sting",
              "pop"  : "billy joel"
            },
          "film" :
            { "color" : "fantasia",
              "black & white" : "pyscho"
            }
        }

sdb = shelve.open("dbshelve")
for (key, value) in list(media.items()):
    sdb[key] = value
print("%s entries in shelf" %len(sdb))    # number of entries
print("keys:", list(sdb.keys()))          # keys in shelf
print("values:", [sdb[key] for key in sdb.keys()])
sdb.close()

#################################################
#
#    $ shelvewrite.py
#    2 entries in shelf
#    keys: ['film', 'music']
#    values: [{'color': 'fantasia', 'black & white': 'pyscho'}, 
#    {'jazz': 'miles davis', 'pop': 'billy joel', 'rock': 'sting'}]
#
