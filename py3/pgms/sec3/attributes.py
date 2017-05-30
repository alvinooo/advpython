#!/usr/bin/env python3
# attributes.py - Accessing attributes
import math

class Polar(object):
    __slots__ = ("radius", "theta", "x", "y")
    def __init__(self, radius, theta):
        self.radius = radius
        self.theta = theta
    def __getattr__(self, name):
        if name == "x":
            return self.radius* math.cos(self.theta)
        if name == "y":
            return self.radius* math.sin(self.theta)
        return super().__getattr__(name)

    def __setattr__(self, name, value):
        if name in Polar.__slots__[2:]:
            raise TypeError("Polar %s is readonly" %name)
        if name == "radius" and value <= 0:
            raise ValueError("Polar has bad radius %g" %value)
        super().__setattr__(name, value)
        
polar = Polar(20, 45)
print(polar.radius, polar.theta, polar.x, polar.y)
polar.radius = 30; polar.theta = 60
print(polar.radius, polar.theta, polar.x, polar.y)
#polar.radius = -100
#polar.rad = 100

#################################################
#
#    $ attributes.py
#    20 45 10.5064397764 17.0180704907
#    30 60 -28.5723894125 -9.14431863307
#
