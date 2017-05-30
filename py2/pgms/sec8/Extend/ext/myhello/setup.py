#!/usr/bin/env python
# setup.py - helloworld module
from distutils.core import setup, Extension

setup(name="myhello", 
    version="1.0",
    ext_modules=[Extension("myhello", ["myhello.c", "myfuncs.c"])])

###########################################
#
#     $ setup.py build_ext --inplace
#
