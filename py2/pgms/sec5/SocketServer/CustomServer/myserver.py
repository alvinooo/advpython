#!/usr/bin/env python
# myserver.py - server objects 
import sys
from Server import Server
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)
server = Server(address)

log(DEBUG, "%s %d running..." %address)
try:
    server.run()
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)

###################################################
#
#     $ myserver.py
#     Server: __init__
#     Server: server_activate
#     Server: localhost 2500 running...
#     Server: waiting for requests
#
#     ^C
#     Server: stopped
#     $
#
