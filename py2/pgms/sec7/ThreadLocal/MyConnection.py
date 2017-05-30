# MyConnection.py - MyConnection module
from socket import *
from threading import *

class MyConnection():
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.__address = address
        self.__family = family
        self.__type = type
        self.__local = local()      # thread local

    def __enter__(self):
        if hasattr(self.__local, "sock"): 
            raise RunTimeError("Already connected")
        self.__local.sock = socket(self.__family, self.__type)
        self.__local.sock.connect(self.__address)
        return self.__local.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.__local.sock.close()
        del self.__local.sock

