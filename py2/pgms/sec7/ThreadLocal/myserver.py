#!/usr/bin/env python
# myserver.py - TCP server
import sys
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024
conn = None

sock = socket(AF_INET, SOCK_STREAM)
address = (HOST, PORT)
sock.bind(address)
sock.listen(5)

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        (conn, addr) = sock.accept()
        log(DEBUG, "connection from %s %d" %addr)
        data = conn.recv(MAXDATA)
        data = data.upper()     # make data uppercase
        conn.sendall(data)
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)
finally:
    if conn is not None:
        conn.close()

#####################################
#
#     $ myserver.py
#     Server: localhost 2500 running...
#
#     ^C
#     Server: stopped
#     $
