# Server.py - TCP Server module
from socket import *
QUEUE = 5
MAXDATA = 1024

class Server(object):
    def __init__(self, addr):
        self.__serverAddr = addr
        self.__conn = None
        self.__clientAddr = None
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sock.bind(addr)
        self.__sock.listen(QUEUE)
    def __del__(self):
        if self.__conn is not None: 
            self.__conn.close()
        self.__sock.close()
        
    def accept(self): 
        (self.__conn, self.__clientAddr) = self.__sock.accept()
    def getClientAddr(self): return self.__clientAddr
    def getConnection(self): return self.__conn
    def send(self, data): 
        if self.__conn is not None: 
            self.__conn.sendall(data)
    def receive(self): 
        if self.__conn is not None: 
            return self.__conn.recv(MAXDATA)
    def __str__(self): return "%s %d" %self.__serverAddr

