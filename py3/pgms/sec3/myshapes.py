#!/usr/bin/env python3
# myshapes.py - Shape hierarchy
import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
    def area(self):
        return math.pi * self.__radius**2 
    def circum(self):
        return 2 * math.pi * self.__radius
    def __str__(self):        # string method
        return "Circle: radius = %s" %self.__radius

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side
    def area(self):
        return self.__side**2 
    def circum(self):
        return 4 * self.__side
    def __str__(self):        # string method
        return "Square: side = %s" %self.__side

shapes = [Circle(10), Square(5)]
print("number of shapes = %d" %Shape.numShapes())
Shape.show(shapes)
del shapes                    # remove all shapes
print("number of shapes = %d" %Shape.numShapes())

#################################################
#
#    $ myshapes.py
#    number of shapes = 2
#    Circle: radius = 10 with area = 314.159, circum = 62.8319
#    Square: side = 5 with area = 25, circum = 20
#    number of shapes = 0
#
