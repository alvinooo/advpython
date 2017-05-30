#!/usr/bin/env python
# myclient.py - TCP SSL client
import sys, ssl
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500

sock = socket(AF_INET, SOCK_STREAM)
sslSocket = ssl.wrap_socket(sock,
    ca_certs = "mycert", cert_reqs = ssl.CERT_REQUIRED)
    #certfile = "mycert", cert_reqs = ssl.CERT_REQUIRED)

address = (HOST, PORT)
try:
    sslSocket.connect(address)
except ssl.SSLError as ex:
    msg = str(ex)
    log(DEBUG, "%s" %msg[msg.find(": ")+2:])
    sys.exit(1)
    
log(DEBUG, "%s %d connected..." %address)
try:
    data = "Message from secure socket"
    log(DEBUG, "sent %s" %data)
    sslSocket.write(data)
finally:
    sslSocket.close()

#####################################
#
#     $ myclient.py
#     Server: connection from 127.0.0.1 42853
#     Client: localhost 2500 connected...
#     Client: sent Message from secure socket
#     Server: received Message from secure socket
#
