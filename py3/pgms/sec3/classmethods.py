#!/usr/bin/env python3
# classmethods.py - class methods

def myPhoneData(name):
    data = { "rick" : [303, 732, 9276], "bob" : [212, 439, 5629],
             "jack" : [404, 472, 6512] }
    return data[name]

class Phone:
    def __init__(self, areacode, prefix, number):
        self.__areacode = areacode
        self.__prefix = prefix
        self.__number = number
    @classmethod
    def findNumber(cls, name):
        pd = myPhoneData(name)
        return cls(pd[0], pd[1], pd[2]) 
    def getAreaCode(self): return self.__areacode
    def getPrefix(self): return self.__prefix
    def getNumber(self): return self.__number
    def __str__(self):
        return "%3d-%3d-%4d" %(self.getAreaCode(), 
            self.getPrefix(), self.getNumber())

class MobilePhone(Phone):
    def __str__(self):
        return "(%3d) %3d-%4d" %(self.getAreaCode(), 
            self.getPrefix(), self.getNumber())
    
phone1 = Phone.findNumber("bob")
print(phone1)
phone2 = MobilePhone.findNumber("bob")
print(phone2)

#################################################
#
#    $ classmethods.py
#    212-439-5629
#    (212) 439-5629
#
