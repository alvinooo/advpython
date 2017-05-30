#!/usr/bin/env python
# pickledict.py - dictionary serialization
import pickle
from pprint import pprint

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

print "Before: ",
pprint(media)                    # show dictionary

sdata = pickle.dumps(media)      # serialize data
#print sdata
del media                        # remove dictionary

print "After: ",
media = pickle.loads(sdata)      # deserialize data
pprint(media)                    # show dictionary

#################################################
#
#    $ pickledict.py
#    Before: {'film': {'black & white': 'pyscho', 'color': 'fantasia'},
#    'music': {'jazz': 'miles davis', 'pop': 'billy joel', 'rock': 'sting'}}
#    After: {'film': {'black & white': 'pyscho', 'color': 'fantasia'},
#    'music': {'jazz': 'miles davis', 'pop': 'billy joel', 'rock': 'sting'}}
#
