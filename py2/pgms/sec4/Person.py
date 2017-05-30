# Person.py - Person module

class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self): return self.__name
    def getAge(self): return self.__age

    def __str__(self):
        return "Person: %s %d" %(self.__name, self.__age)

