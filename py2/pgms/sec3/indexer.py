#!/usr/bin/env python
# indexer.py - Method overriding

class Indexer:
    def __getitem__(self, index):
        return index ** 3

cubes = Indexer()
for index in range(11):
    print cubes[index],

#################################################
#
#    $ indexer.py
#    0 1 8 27 64 125 216 343 512 729 1000
#
