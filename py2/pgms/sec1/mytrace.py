#!/usr/bin/env python
# mytrace.py - decorator tracing function
from tracing import *

#trace["enable"] = False

@tracing
def intersect(arg1, arg2):
    common = []
    for arg in arg1:
        if arg in arg2:
            common.append(arg)
    return common

@tracing
def max(*args):
    result = list(args)
    result.sort()
    return result[-1]

print max(22, 63, 43, 10)
print max("track", "zulu", "able")

print intersect([1, 2, 3, 4], (2, 4, 6, 8))
print intersect([13, 25, 44], (25, 55))

#####################################
#
#     $ mytrace.py
#     63
#     zulu
#     [2, 4]
#     [25]
#
#     $ cat logfile
#     Invoking max: (22, 63, 43, 10) {}
#     max returned from: 63
#     Invoking max: ('track', 'zulu', 'able') {}
#     max returned from: zulu
#     Invoking intersect: ([1, 2, 3, 4], (2, 4, 6, 8)) {}
#     intersect returned from: [2, 4]
#     Invoking intersect: ([13, 25, 44], (25, 55)) {}
#     intersect returned from: [25]
#      
