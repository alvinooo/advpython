#!/usr/bin/env python
# mylist.py - working with lists

# the verbose way
cubes = []
for n in range(1,6):
    cubes.append(n**3)
print cubes

# using lambda and map
cubes = map(lambda n : n**3, range(1,6))
print cubes

# using list comprehensions
cubes = [n**3 for n in range(1,6)]
print cubes

#####################################
#
#     $ mylist.py
#     [1, 8, 27, 64, 125]
#     [1, 8, 27, 64, 125]
#     [1, 8, 27, 64, 125]
#
