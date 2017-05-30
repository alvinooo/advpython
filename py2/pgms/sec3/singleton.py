#!/usr/bin/env python
# singleton.py - Singleton metaclass, default constr

class Singleton(type): 
    def __init__(self, name, bases, attrs):
        print "Singleton constr"
        super(Singleton, self).__init__(name, bases, attrs)
        self._instance = None
    def __call__(self):
        if self._instance is None:
            print "creating", self.__name__
            self._instance = super(Singleton, self).__call__()
        return self._instance

class MySingleton(object):
    __metaclass__ = Singleton
    def __init__(self):
        print "MySingleton constr"
    def write(self, data):
        print "write " + data

one = MySingleton()
print "addr one: %x" %id(one)
two = MySingleton()
print "addr two: %x" %id(two)
one.write("data")

#################################################
#
#    $ singleton.py
#    Singleton constr
#    creating MySingleton
#    MySingleton constr
#    addr one: b7276c8c
#    addr two: b7276c8c
#    write data
#
