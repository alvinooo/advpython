#!/usr/bin/env python
# descriptors.py - Data descriptors
from weakref import WeakKeyDictionary

class RangeProperty(object):
    def __init__(self, lower, upper):
        self.__values = WeakKeyDictionary()
        self.__lower = lower
        self.__upper = upper
    def __get__(self, instance, cls):
        if instance is None: return self
        return self.__values.get(instance, self.__lower)
    def __set__(self, instance, value):
        if value < self.__lower or value > self.__upper:
            raise ValueError("RangeProperty %d not between %d and %d" \
                %(value, self.__lower, self.__upper))
        self.__values[instance] = value
    def __delete__(self, instance):
        raise AttributeError("can't delete RangeProperty attribute")
        
class MyClass(object):
    num1 = RangeProperty(-10, 10)
    num2 = RangeProperty(0, 100)
    num3 = RangeProperty(100, 500)

one = MyClass()
print one.num1, one.num2, one.num3
one.num2 = 25
print one.num1, one.num2, one.num3
two = MyClass()
two.num2 = 75
print two.num1, two.num2, two.num3
#one.num2 = 500              # out of range
#del one.num1                # delete attribute

#################################################
#
#    $ descriptors.py
#    -10 0 100
#    -10 25 100
#    -10 75 100
#
