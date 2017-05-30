#!/usr/bin/env python
# myclient.py - TCP SSL client
import socket
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (HOST, PORT)
sock.connect(address)
log(DEBUG, "%s %d connected..." %address)

try:
    data = "Message from secure socket"
    sslSocket = socket.ssl(sock)
    log(DEBUG, "Server is %s" %sslSocket.server())
    log(DEBUG, "Issuer is %s" %sslSocket.issuer())
    log(DEBUG, "sent %s" %data)
    sslSocket.write(data)
finally:
    sock.close()

#####################################
#
#     $ myclient.py
#     Server: connection from 127.0.0.1 42855
#     Client: localhost 2500 connected...
#     Client: Server is /C=US/ST=California/L=San Diego/O=ASG/CN=Paul
#     Client: Issuer is /C=US/ST=California/L=San Diego/O=ASG/CN=Paul
#     Client: sent Message from secure socket
#     Server: received Message from secure socket
#
