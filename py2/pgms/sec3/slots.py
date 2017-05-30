#!/usr/bin/env python
# slots.py - slots
import math

class Polar(object):
    __slots__ = ("radius", "theta")
    def __init__(self, radius, theta):
        self.radius = radius
        self.theta = theta
    def getx(self):
        return self.radius * math.cos(self.theta)
    def gety(self):
        return self.radius * math.sin(self.theta)

polar = Polar(20, 45)
print polar.radius, polar.theta
print polar.getx(), polar.gety()

polar.radius = 30
polar.theta = 60
print polar.radius, polar.theta
print polar.getx(), polar.gety()

#################################################
#
#    $ slots.py
#    20 45
#    10.5064397764 17.0180704907
#    30 60
#    -28.5723894125 -9.14431863307
#
