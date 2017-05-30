#!/usr/bin/env python3
# parents.py - Initializing parent classes

class MyBase():           # new style class by default
    def __init__(self, value):
        self.__value = value

class MyDerived(MyBase):
    def __init__(self, value):
        #MyBase.__init__(self, value)    # initialize parent
        super().__init__(value)          # Python 3.X 

derived = MyDerived(12)
print(derived)

#################################################
#
#    $ parents.py
#    <__main__.MyDerived object at 0x8471c6c>
#
