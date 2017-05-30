#!/usr/bin/env python3
# mycopy.py - copy files
import sys
from os import *
from mmap import *

if (len(sys.argv) != 3):
    raise SystemExit("Usage: %s file1 file2" %sys.argv[0])

# your code here...

###############################################
#
#    $ mycopy.py
#    Usage: ./mycopy.py file1 file2
#
#    $ mycopy.py file1 file2
#     
