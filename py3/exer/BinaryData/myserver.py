#!/usr/bin/env python3
# myserver.py - TCP server, binary data
import os, sys, socket, codecs
from struct import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 4096
packer = Struct("I")         # file length 
conn = None                  # client connection

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (HOST, PORT)
sock.bind(address)
sock.listen(5)

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        # your code here...
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
#
