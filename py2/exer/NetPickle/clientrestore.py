#!/usr/bin/env python
# clientrestore.py - restore client object
import sys, pickle
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

filename = sys.argv[1]
# your code here...

log(DEBUG, "connected...")
message = "Here's a message."
log(DEBUG, "sending %s" %message)
client.send(message)
data = client.receive()
log(DEBUG, "received %s" %data)

###################################################
#
#     $ clientrestore.py sclient
#     Client: __setstate__() connection
#     Client: deserialized localhost 2500
#     Client: connected...
#     Client: sending Here's a message.
#     Server: received Here's a message.
#     Server: sent HERE'S A MESSAGE.
#     Client: received HERE'S A MESSAGE.
#
