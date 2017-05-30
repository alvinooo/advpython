#!/usr/bin/env python
# lambdalist.py - list of lambdas

mylist = []
mylist.append(lambda x : x * 2)
mylist.append(lambda x : x * 3)
mylist.append(lambda x : x**2)
mylist.append(lambda x : x**3)

print mylist[0](3), mylist[3](10)

for func in mylist:
    print func(5),
print

#####################################
#
#     $ lambdalist.py
#     6 1000
#     10 15 25 125
#      
