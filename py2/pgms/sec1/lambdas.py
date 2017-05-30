#!/usr/bin/env python
# lambdas.py - lambdas
import sys

noargs = lambda : sys.stdout.write("default\n")
noargs()

mary = lambda n : sys.stdout.write("%s\n" %n)
mary("lambda")

def myadd(x, y) : return x + y
add = myadd
result = add(3, 4)
print result

add = lambda x,y : x + y
result = add(3, 4)
print result

result = add("alpha", "bet")
print result

mult = lambda x,y : x * y
result = mult(3, 4)
print result

result = mult("No", 4)
print result

teenager = lambda age : age >= 13 and age <= 19
if teenager(15): print "teenager"
if not teenager(30): print "not a teenager"

names = ["Manny", "Moe", "Jack"]
names.sort(key=lambda x : len(x))
#names.sort()
print names

#####################################
#
#     $ lambdas.py
#     default
#     lambda
#     7
#     7
#     alphabet
#     12
#     NoNoNoNo
#     teenager
#     not a teenager
#     ['Moe', 'Jack', 'Manny']
#      
