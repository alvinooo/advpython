#!/usr/bin/env python
# myfiles.py - MyFile with protected, public access
from MyFile import MyFile
from MyOtherFile import MyOtherFile

try:
    file = MyFile("tester")
    #file = MyFile("tester", crypt=True)
    print "MyFile:", file.getName()
    print "Crypting:", file.crypt
    file.write("my data")
    print file.read(),
    #file.encrypt("abc")

    mfile = MyOtherFile("mtester")
    mfile.show("my data")
    #mfile.encrypt("abc")

except Exception as ex:
    raise SystemExit("%s: %s" %(ex.__class__.__name__, ex))

#################################################
#
#    $ myfiles.py
#    MyFile: tester
#    Crypting: False
#    my data
#    encrypting
#    zl qngn
#
