#!/usr/bin/env python
# pickleread.py - object deserialization
import sys, pickle

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

filename = sys.argv[1]
with open(filename, "rb") as file:
    while True:
        try:
            obj = pickle.load(file)    # deserialize from file
        except EOFError: 
            break
        print "Deserializing", obj

#################################################
#
#    $ pickleread.py sdata
#    Deserializing Person: Bob 45
#    Deserializing Circle: 10
#
