#!/usr/bin/env python
# decorator2.py - method decorators
from tracing import *

class MyClass(object):
    @tracing
    def square(self, num): return num ** 2

    @classmethod
    @tracing
    def cube(cls, num): return num ** 3

    @staticmethod
    @tracing
    def quad(num): return num ** 4

print MyClass().square(3), MyClass.cube(4), MyClass.quad(5)

#################################################
#
#    $ decorator2.py
#    9 64 625
#
#    $ cat logfile
#    Invoking square: (<__main__.MyClass object at 0x8ac0e0c>, 3) {}
#    square returned from: 9
#    Invoking cube: (<class '__main__.MyClass'>, 4) {}
#    cube returned from: 64
#    Invoking quad: (5,) {}
#    quad returned from: 625
#
