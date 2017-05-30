#!/usr/bin/env python
# setup.py - helloworld module
from distutils.core import setup, Extension

setup(name="myext", 
    version="1.0",
    ext_modules=[Extension("myext", ["myext.c", "myfuncs.c"])])

###########################################
#
#     $ setup.py build_ext --inplace
#
