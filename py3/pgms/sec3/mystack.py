#!/usr/bin/env python3
# mystack.py - Stack class

class Stack(object):
    def __init__(self):
        self.__stack = []
    def push(self, data):
        self.__stack.append(data)
    def pop(self):
        return self.__stack.pop()
    def length(self):
        return len(self.__stack)
    def empty(self):
        return self.length() == 0

st = Stack()
for mydata in ("name", 45, 185.5, (2,4,6)):
    st.push(mydata)
print("Stack has %d items" %st.length())
while not st.empty():
    print(st.pop())

#################################################
#
#    $ mystack.py
#    Stack has 4 items
#    (2, 4, 6)
#    185.5
#    45
#    name
#
