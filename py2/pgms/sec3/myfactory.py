#!/usr/bin/env python
# myfactory.py - create objects dynamically
import Factory

obj = Factory.createObject()
obj.method()

#################################################
#
#    $ cat classnames
#    MyClasses.Thing 12 filename
#
#    $ myfactory.py
#    Thing: 12 filename
#
#    $ cat classnames
#    MyClasses.OtherThing 3.4
#
#    $ myfactory.py
#    OtherThing: 3.4
#
