#!/usr/bin/env python
# singleton2.py - Singleton metaclass, arg constrs, inheritance

class Singleton(type): 
    def __init__(self, *args, **kwargs):
        print "Singleton constr"
        super(Singleton, self).__init__(*args, **kwargs)
        self._instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            print "creating", self.__name__
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance

class MySingleton(object):
    __metaclass__ = Singleton
    def __init__(self, *args, **kwargs):
        print "MySingleton constr", args, kwargs
    def write(self, data):
        print "write " + data

class OtherSingleton(MySingleton):
    def __init__(self, *args, **kwargs):
        super(OtherSingleton, self).__init__(*args, **kwargs)
        print "OtherSingleton constr", args, kwargs

one = MySingleton(3.4)
print "addr one: %x" %id(one)
two = MySingleton(12, "abc")
print "addr two: %x" %id(two)
one.write("data")
three = OtherSingleton("last")
print "addr three: %x" %id(three)

#################################################
#
#    $ singleton2.py
#    Singleton constr
#    Singleton constr
#    creating MySingleton
#    MySingleton constr (3.4,) {}
#    addr one: 8878e6c
#    addr two: 8878e6c
#    write data
#    creating OtherSingleton
#    MySingleton constr ('last',) {}
#    OtherSingleton constr ('last',) {}
#    addr three: 8878e4c
#
