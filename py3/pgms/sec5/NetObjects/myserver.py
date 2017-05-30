#!/usr/bin/env python3
# myserver.py - server objects
import sys
from Server import Server
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)
server = Server(address)       # Server object

log(DEBUG, "%s running..." %server)
try:
    while True:
        server.accept()
        addr = server.getClientAddr()
        log(DEBUG, "connection from %s %d" %addr)
        data = server.receive()
        log(DEBUG, "received %s" %data)
        data = data.upper()    # make data uppercase
        server.send(data)
        log(DEBUG, "sent %s" %data)
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)

###################################################
#
#     $ myserver.py
#     Server: localhost 2500 running...
#
#     ^C
#     Server: stopped
#     $
#
