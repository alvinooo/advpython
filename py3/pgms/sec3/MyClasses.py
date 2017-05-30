# MyClasses.py - Classes

class Thing:
    def __init__(self, num, name):
        self.__num = num
        self.__name = name
    def method(self):
        print("Thing: %s %s" %(self.__num, self.__name))

class OtherThing:
    def __init__(self, val):
        self.__val = val
    def method(self):
        print("OtherThing: %s" %self.__val)
