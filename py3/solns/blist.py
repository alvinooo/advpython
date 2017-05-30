#!/usr/bin/env python3
# blist.py - Bounded list
from BoundList import BoundList

try:
    blist = BoundList(2000, 2009)
    print("lower bound = %d" %blist.lower)
    print("upper bound = %d" %blist.upper)
    print("length is %d" %blist.length())

    for (val, index) in enumerate(blist.getRange()):
        blist[index] = val              # setter

    for index in blist.getRange():
        print(blist[index], end=' ')             # getter
    print()
    blist[1000] = 10                    # out of bounds
except Exception as ex:
    raise SystemExit("%s" %ex)
    
#################################################
#
#    $ blist.py
#    lower bound = 2000
#    upper bound = 2009
#    length is 10
#    0 1 2 3 4 5 6 7 8 9
#    BoundList has bad index 1000

