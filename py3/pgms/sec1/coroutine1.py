#!/usr/bin/env python3
# coroutine1.py - coroutines

def printMatch(text):
    print("matching", text)
    while True:
        line = yield       # receive 
        if text in line:
            print(line)

myMatch = printMatch("linux")
next(myMatch)       # advance to first yield

myMatch.send("working on windows")
myMatch.send("linux version")
myMatch.send("macOs libraries") 
myMatch.close()

#####################################
#
#     $ coroutine1.py
#     matching linux
#     linux version
#      
