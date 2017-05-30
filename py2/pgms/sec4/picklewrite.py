#!/usr/bin/env python
# picklewrite.py - object serialization
import sys, pickle
from Person import Person
from Circle import Circle

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

p1 = Person("Bob", 45)           # Person object
c1 = Circle(10)                  # Circle object

filename = sys.argv[1]
with open(filename, "wb") as file:
    for obj in (p1, c1):
        print "Serializing", obj
        pickle.dump(obj, file)   # serialize to file

#################################################
#
#    $ picklewrite.py sdata
#    Serializing Person: Bob 45
#    Serializing Circle: 10
#
