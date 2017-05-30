# Client.py - TCP Client module
from socket import *
MAXDATA = 1024

class Client(object):
    def __init__(self, addr):
        self.__ServerAddr = addr
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sock.connect(addr)
    def __del__(self): 
        self.__sock.close()
        
    def send(self, data): 
        self.__sock.sendall(data.encode("ascii"))
    def receive(self): 
        return self.__sock.recv(MAXDATA).decode("ascii")
    def __str__(self): return "%s %d" %self.__ServerAddr

