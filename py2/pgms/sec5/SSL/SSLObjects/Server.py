# Server.py - TCP SSL Server module
import ssl
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class Server(object):
    def __init__(self, addr, cert):
        self.__serverAddr = addr
        self.__cert = cert
        self.__conn = None
        self.__clientAddr = None
        self.__sslSocket = None
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sock.bind(addr)
        self.__sock.listen(5)
    def __del__(self):
        if self.__conn is not None: 
            self.__conn.close()
        if self.__sslSocket is not None: 
            self.__sslSocket.close()
        
    def accept(self): 
        try:
            (self.__conn, self.__clientAddr) = self.__sock.accept()
            self.__sslSocket = ssl.wrap_socket(self.__conn,
                server_side = True, certfile = self.__cert)
            return True
        except ssl.SSLError as ex:
            msg = str(ex)
            log(DEBUG, "%s" %msg[msg.find(": ")+2:])
            if self.__conn is not None: 
                self.__conn.close()
            return False
            
    def getClientAddr(self): return self.__clientAddr
    def getConnection(self): return self.__conn
    def getCertificate(self): return self.__cert
    def send(self, data): 
        if self.__sslSocket is not None: 
            self.__sslSocket.write(data)
    def receive(self): 
        if self.__sslSocket is not None: 
            return self.__sslSocket.read()
    def __str__(self): return "%s %d" %self.__serverAddr

