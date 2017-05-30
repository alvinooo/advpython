#!/usr/bin/env python3
# serializer.py - Serialize objects
from Serializable import Serializable, deserialize

class Polar(Serializable):
    def __init__(self, radius, theta):
        super(Polar, self).__init__(radius, theta)
        self.radius = radius
        self.theta = theta
    def __str__(self):
        return "Polar(%d, %d)" %(self.radius, self.theta)

polar = Polar(20, 45)
print("Object: ", polar)
data = polar.serialize()
print("Serialized: ", data)
print("Deserialized:", deserialize(data))

#################################################
#
#    $ serializer.py
#    Object:  Polar(20, 45)
#    Serialized:  {"class": "Polar", "args": [20, 45]}
#    Deserialized: Polar(20, 45)
#
