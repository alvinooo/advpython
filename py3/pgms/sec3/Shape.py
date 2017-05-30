# Shape.py - Abstract base class
import sys
from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    __count = 0
    def __init__(self):
        Shape.__count += 1
    def __del__(self):
        Shape.__count -= 1
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def circum(self): pass
    @staticmethod
    def numShapes():
        return Shape.__count
    @staticmethod
    def show(shapes, func=sys.stdout.write):
        for shape in shapes:
            func("%s with area = %g, circum = %g\n" \
                %(shape, shape.area(), shape.circum()))
