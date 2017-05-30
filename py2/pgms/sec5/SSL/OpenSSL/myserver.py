#!/usr/bin/env python
# myserver.py - TCP SSL server
import sys
from OpenSSL import SSL
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file("key")
context.use_certificate_file("cert")

sock = socket(AF_INET, SOCK_STREAM)
sock = SSL.Connection(context, sock)

address = (HOST, PORT)
sock.bind(address)
sock.listen(5)
conn = None

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        (conn, addr) = sock.accept()
        log(DEBUG, "connection from %s %d" %addr)
        data = conn.recv(MAXDATA)
        log(DEBUG, "received %s" %data)
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
#
