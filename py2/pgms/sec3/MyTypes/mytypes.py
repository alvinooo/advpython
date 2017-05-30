#!/usr/bin/env python
# mytypes.py - Property types with metaclass
from MyType import MyType, PropertyType

class Person(MyType):
    name = PropertyType(str, "Jeff")
    age = PropertyType(int, 21)

person = Person()
print person.name, person.age

person.name = "Bob"
person.age = 33
print person.name, person.age

#person.age = "Jim"

#################################################
#
#    $ mytypes.py
#    TypeMeta: __new__ MyType
#    PropertyType: __init__ <type 'str'>
#    PropertyType: __init__ <type 'int'>
#    TypeMeta: __new__ Person
#    Jeff 21
#    Bob 33
#
