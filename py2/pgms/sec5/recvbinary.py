#!/usr/bin/env python
# recvbinary.py - receive TCP binary data
import sys, binascii
from socket import *
from struct import *
from logging import *
basicConfig(level=DEBUG, format="Receiver: %(message)s",)

HOST = "localhost"
PORT = 2500

unpacker = Struct("i 28s f")
psize = unpacker.size
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
        pdata = conn.recv(psize)
        log(DEBUG, binascii.hexlify(pdata))
        data = unpacker.unpack(pdata)
        log(DEBUG, data)
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)
finally:
    if conn is not None:
        conn.close()

#####################################
#
#     $ recvbinary.py
#     Receiver: localhost 2500 running...
#
#     ^C
#     Receiver: stopped
#     $
