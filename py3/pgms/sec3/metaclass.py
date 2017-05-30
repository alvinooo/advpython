#!/usr/bin/env python3
# metaclass.py - Metaclasses

class MetaClass(type): 
    def __new__(cls, name, bases, attrs):
        print("MetaClass.__new__: ", cls)
        return super().__new__(cls, name, bases, attrs)
    def __init__(self, name, bases, attrs):
        print("MetaClass.__init__: ", self)
        super().__init__(name, bases, attrs)
    def __call__(self):
        print("MetaClass.__call__: ", self)
        super().__call__()

class MyClass(object, metaclass=MetaClass):
    def __init__(self):
        print("MyClass.__init__: ", self)

one = MyClass()

#################################################
#
#    $ metaclass.py
#    MetaClass.__new__:  <class '__main__.MetaClass'>
#    MetaClass.__init__:  <class '__main__.MyClass'>
#    MetaClass.__call__:  <class '__main__.MyClass'>
#    MyClass.__init__:  <__main__.MyClass object at 0x9bbcdac>
#
