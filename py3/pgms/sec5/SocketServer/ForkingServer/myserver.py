#!/usr/bin/env python3
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
#     Server: localhost 2500 running...
#     Server: waiting for commands
#
#     ^C
#     Server: stopped
#     $
#
