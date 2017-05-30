#!/usr/bin/env python
# sighandler.py - signal handlers
import sys
from signal import *

handler = lambda signum, frame : myexit(signum, frame, old)

def myexit(signum, frame, oldHandler):
    signal(SIGINT, oldHandler)      # restore handler
    input = raw_input("\nTo quit, type q:")
    try:
        if input == "q": sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
    signal(SIGINT, handler)

old = getsignal(SIGINT)            # get previous handler
signal(SIGINT, handler)

print "running..."
try:
    while True:
        pass
except KeyboardInterrupt:
    print "\nexiting..."
    sys.exit(1)

#####################################
#
#     $ sighandler.py
#
