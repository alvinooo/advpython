#!/usr/bin/env python
# myserver.py - UDP server
import sys, Books
from socket import *
from logging import *
basicConfig(level=ERROR, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024

sock = socket(AF_INET, SOCK_DGRAM)
address = (HOST, PORT)
sock.bind(address)

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        (sql, addr) = sock.recvfrom(MAXDATA)
        log(DEBUG, "%s from %s" %(sql, addr))
        output = Books.run(sql)
        log(DEBUG, output)
        sock.sendto(output, addr)
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)
finally:
    sock.close()

#####################################
#
#     $ myserver.py
#
