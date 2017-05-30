#!/usr/bin/env python
# genkey.py - generate key for ssl
from subprocess import call

cmd = "openssl genrsa 1024 > key"
retval = call(cmd, shell=True)

#################################################
#
#    $ genkey.py
# 
