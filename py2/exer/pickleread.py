#!/usr/bin/env python
# pickleread.py - object deserialization
import sys, Serialize

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

file = sys.argv[1]
mydata = Serialize.restore(file)    # deserialize data
print "Restoring",
for obj in mydata:
    print obj,
print

######################################################
#
#    $ pickleread.py mydata
#    Restoring red 6.3 (10, 20, 30) Person: Bob 45 Circle: 10
#
