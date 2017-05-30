# Circle.py - Circle module
import math

class Circle(object):
    def __init__(self, radius=1):
        self.__radius = radius

    def getRadius(self): return self.__radius
    def circum(self): return 2 * math.pi * self.__radius
    def area(self): return math.pi * self.__radius ** 2

    def __str__(self):
        return "Circle: %s" %(self.__radius)

