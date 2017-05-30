#!/usr/bin/env python
# newclass.py - Create new class

"""
class Square(object):
    def __init(self, side):
        self.__side = side
    def area(self):
        return self.__side**2 
"""

# class name, base classes, attribute dictionary
name = "Square"
bases = (object,)
attrs = {}

# class body
body = """
def __init__(self, side):
    self.__side = side
def area(self):
    return self.__side**2
"""
# execute class body in attribute dictionary
exec(body, globals(), attrs)

# create class
Square = type(name, bases, attrs)

# create object
square = Square(12)
print square.area()

#################################################
#
#    $ newclass.py
#    144
#
