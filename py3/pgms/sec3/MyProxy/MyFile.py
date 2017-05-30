# MyFile.py - protected, public access
import codecs
from Protected import *

class MyFile(Protected):
    __public__ = ["crypt"]
    def __init__(self, name, crypt = False):
        self.name = name
        self.crypt = crypt

    def encrypt(self, data):
        print("encrypting")
        return codecs.encode(data, "rot-13")

    def decrypt(self, data):
        print("decrypting")
        return codecs.encode(data, "rot-13")

    @public
    def write(self, data):
        fp = open(self.name, "w")
        if self.crypt:
            data = self.encrypt(data)
        fp.write("%s\n" %data)
        fp.close()

    @public
    def read(self):
        fp = open(self.name, "r")
        data = fp.read()
        fp.close()
        if self.crypt:
            data = self.decrypt(data)
        return data

    @public
    def getName(self):
        return self.name

