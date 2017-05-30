#!/usr/bin/env python
# mypgm.py - myhello extension module
import myhello            # import C extension

myhello.greeting()        # invoke C function

###########################################
#
#     $ mypgm.py
#     C: initializing myhello module
#     hello there, from C
#
