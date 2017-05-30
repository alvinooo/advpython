#!/usr/bin/env python3
# myfifo.py - Fifo class

class Fifo(object):
    def __init__(self):
        self.__fifo = []
    def write(self, data):
        self.__fifo.append(data)
    def read(self):
        return self.__fifo.pop(0)
    def length(self):
        return len(self.__fifo)
    def empty(self):
        return self.length() == 0

fifo = Fifo()
for mydata in ("name", 45, 185.5, (2,4,6)):
    fifo.write(mydata)
print("Stack has %d items" %fifo.length())
while not fifo.empty():
    print(fifo.read())

#################################################
#
#    $ myfifo.py
#    Stack has 4 items
#    name
#    45
#    185.5
#    (2, 4, 6)
#
