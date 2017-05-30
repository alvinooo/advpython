#!/usr/bin/env python
# imperative.py - imperative design

cost = 0
for line in open("prices.txt"):
    fields = line.split()
    cost += float(fields[1]) * float(fields[2])
print cost

#####################################
#
#     $ imperative.py
#     262633.5
#
