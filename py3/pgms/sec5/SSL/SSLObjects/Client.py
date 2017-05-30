# Client.py - TCP SSL Client module
import ssl
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

class Client(object):
    def __init__(self, addr, cert):
        self.__serverAddr = addr
        self.__cert = cert
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__sslSocket = ssl.wrap_socket(self.__sock,
            ca_certs = cert, cert_reqs = ssl.CERT_REQUIRED)
    def __del__(self): 
        self.__sslSocket.close()
        
    def connect(self):
        try:
            self.__sslSocket.connect(self.__serverAddr)
            return True
        except ssl.SSLError as ex:
            msg = str(ex)
            log(DEBUG, "%s" %msg[msg.find(": ")+2:])
            return False

    def send(self, data): 
        self.__sslSocket.write(data.encode("ascii"))
    def receive(self): 
        return self.__sslSocket.read().decode("ascii")
    def __str__(self): return "%s %d" %self.__serverAddr

