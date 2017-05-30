#!/usr/bin/env python3
# picklewrite.py - object serialization
import sys, Serialize
from Person import Person
from Circle import Circle

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

p1 = Person("Bob", 45)           # Person object
c1 = Circle(10)                  # Circle object
mydata = ["red", 6.3, (10, 20, 30), p1, c1]

file = sys.argv[1]
Serialize.save(file, mydata)     # serialize data
print("Saving", end=' ')
for obj in mydata:
    print(obj, end=' ')
print()

########################################################
#
#    $ picklewrite.py mydata
#    Saving red 6.3 (10, 20, 30) Person: Bob 45 Circle: 10
#
