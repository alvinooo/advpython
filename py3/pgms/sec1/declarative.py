#!/usr/bin/env python3
# declarative.py - declarative design

lines = open("prices.txt")
fields = [line.split() for line in lines]
cost = sum([float(field[1]) * float(field[2]) for field in fields])
print(cost)

#####################################
#
#     $ declarative.py
#     262633.5
#
