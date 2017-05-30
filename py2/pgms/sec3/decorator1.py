#!/usr/bin/env python
# decorator1.py - class decorator

registry = {}
def register(cls):
    registry[cls.__name__] = cls
    return cls

@register
class MyClass(object):
    def __init__(self):
        print "MyClass constr"
    def write(self, data):
        print "write " + data
# implemented as: MyClass = register(MyClass)

one = MyClass()
one.write("data")
print registry

#################################################
#
#    $ decorator1.py
#    MyClass constr
#    write data
#    {'MyClass': <class '__main__.MyClass'>}
#
