#!/usr/bin/env python
# mypgm.py - myext C++ extension module
import myext

class MyClass(object):
    def __init__(self, num):
        self.__obj = myext.MyClass_new(num)
    def getNum(self):
        return myext.MyClass_getNum(self.__obj)

myobj = MyClass(12)
num = myobj.getNum()
print "Python:", num

###########################################
#
#     $ mypgm.py
#     C++: initializing myext module
#     C++: MyClass constr called
#     C++: MyClass::getNum() called
#     Python: 12
#     C++: MyClass destr called
#
