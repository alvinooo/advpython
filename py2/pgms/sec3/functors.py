#!/usr/bin/env python
# functors.py - Functors

class AddWords(object):
    def __init__(self, word=""):
        self.__word = word
    def __call__(self, word):
        self.__word += word
        return self.__word

mywords = AddWords("this ")         # invokes __init__()
mywords("is ")                      # invokes __call__()
#AddWords.__call__(mywords, "is ")
mywords("an error ")                # invokes __call__()
print mywords("message")

class Offset(object):
    def __init__(self, start):
        self.__start = start
    def __call__(self, num):
        return abs(num - self.__start)
    
nums = [27, 8, -3, 15, 21, -12]
nums.sort(key=Offset(10))
print nums

#################################################
#
#    $ functors.py
#    this is an error message
#    [8, 15, 21, -3, 27, -12]
#
