#!/usr/bin/env python
# myserver.py - server objects
import sys
from Server import Server
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)
server = Server(address, "mycert")       # Server object

log(DEBUG, "%s running..." %server)
try:
    while True:
        if server.accept(): 
            data = server.receive()
            log(DEBUG, "received %s" %data)
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
