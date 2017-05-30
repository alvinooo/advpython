#!/usr/bin/env python
# parents.py - Initializing parent classes

class MyBase(object):        # new style class
#class MyBase():             # old style class
    def __init__(self, value):
        self.__value = value

class MyDerived(MyBase):
    def __init__(self, value):
        #MyBase.__init__(self, value)             # initialize parent
        super(MyDerived, self).__init__(value)   # Python 2.X 

derived = MyDerived(12)
print derived

#################################################
#
#    $ parents.py
#    <__main__.MyDerived object at 0x8471c6c>
#
