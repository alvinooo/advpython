#!/usr/bin/env python3
# factory1.py - Class factories
import sys

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s classname" %sys.argv[0])

class Thing:
    def method(self):
        print("Thing")

class OtherThing:
    def method(self):
        print("OtherThing")

def factory(className):
    instance = globals()[className]
    return instance()

className = sys.argv[1]

var = factory(className)
var.method()

#################################################
#
#    $ factory1.py Thing
#    Thing
#
#    $ factory.py OtherThing
#    OtherThing
