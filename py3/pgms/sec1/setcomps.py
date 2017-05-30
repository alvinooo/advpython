#!/usr/bin/env python3
# setcomps.py - set comprehensions

# list comprehension, duplicates
mylist = [i * j for i in range(1, 5) for j in range(1, 5)]
print(mylist)

# set comprehension, no duplicates
myset = {i * j for i in range(1, 5) for j in range(1, 5)}
mylist = list(myset)
print(mylist)

#####################################
#
#     $ setcomps.py
#     [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
#     [1, 2, 3, 4, 6, 8, 9, 12, 16]
#      
