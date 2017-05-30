#!/usr/bin/env python3
# mypgm.py - call C++ with ctypes
from ctypes import *

# load shared C/C++ library
mylib = CDLL("./libcpp.so")

MyClass_new = mylib.MyClass_new
MyClass_del = mylib.MyClass_del
MyClass_getNum = mylib.MyClass_getNum

class MyClass(object):
    def __init__(self, num):
        self.__obj = MyClass_new(num)
    def __del__(self):
        MyClass_del(self.__obj)
    def getNum(self):
        return MyClass_getNum(self.__obj)

myobj = MyClass(12)
num = myobj.getNum()
print("Python:", num)

#####################################
#
#     $ mypgm.py
#     C++: new MyClass
#     C++: MyClass.getNum()
#     Python: 12
#     C++: delete MyClass obj
#
