# Client.py - TCP Client module
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)
MAXDATA = 1024

class Client(object):
    def __init__(self, addr):
        self.__ServerAddr = addr
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sock.connect(addr)
    def __del__(self): 
        self.__sock.close()
    def __getstate__(self):
        log(DEBUG, "__getstate__() connection")
        return self.__ServerAddr
    def __setstate__(self, value):
        log(DEBUG, "__setstate__() connection")
        self.__ServerAddr = value
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sock.connect(self.__ServerAddr)
        
    def send(self, data): 
        self.__sock.sendall(data.encode("ascii"))
    def receive(self): 
        return self.__sock.recv(MAXDATA).decode("ascii")
    def __str__(self): return "%s %d" %self.__ServerAddr

