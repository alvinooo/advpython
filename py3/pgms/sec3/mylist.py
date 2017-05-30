#!/usr/bin/env python3
# mylist.py - Custom list

class MyList(list):
    def __init__(self, items):
        super().__init__(items)
    def nitems(self):
        counts = {}
        for item in self:
            #if item not in counts: counts[item] = 0
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts

mylist = MyList(["and", "for", "bye", "or", "and", "or"])
print(mylist.pop())
mylist.append("bye")
print(mylist)
print(mylist.nitems())

#################################################
#
#    $ mylist.py
#    or
#    ['and', 'for', 'bye', 'or', 'and', 'bye']
#    {'and': 2, 'bye': 2, 'or': 1, 'for': 1}
#
