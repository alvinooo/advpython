# MyOtherFile.py - protected, public access with inheritance
from Protected import public 
from MyFile import MyFile

class MyOtherFile(MyFile):
    def __init__(self, name, crypt = False):
        super(MyOtherFile, self).__init__(name, crypt)

    @public
    def show(self, data):
        data = self.encrypt(data)
        print data

