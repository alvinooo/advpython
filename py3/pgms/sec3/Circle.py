# Circle.py - Circle class with properties

class Circle(object):
    def __init__(self, radius = 1):   # constructor
        self.radius = radius          # calls setter

    @property
    def radius(self):                 # radius property getter
        return self.__radius          # return radius

    @radius.setter
    def radius(self, radius):         # radius property setter
        if (radius <= 0):
            raise ValueError("Circle has bad radius %d" %radius)
        self.__radius = radius        # instance data


