#!/usr/bin/env python
# dictlambdas.py - lambdas in dictionaries

def f():
    print "f()"

def g(num):
    print "g() with", num

# this is not what we want
mydict = { 1 : f(), 2 : g(2) }
print mydict

# this is what we want
mydict = { 1 : lambda : f(), 2 : lambda(x) : g(x) }
print mydict
mydict[1](), mydict[2](10)

#####################################
#
#     $ dictlambdas.py
#     f()
#     g() with 2
#     {1: None, 2: None}
#     {1: <function <lambda> at 0x93f3374>, 
#      2: <function <lambda> at 0x93f36f4>}
#     f()
#     g() with 10
#      
