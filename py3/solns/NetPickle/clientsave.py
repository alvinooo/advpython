#!/usr/bin/env python3
# clientsave.py - save client object
import sys, pickle
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)

client = Client(address)
log(DEBUG, "%s %d connected..." %address)

client.send("Here's a message")
log(DEBUG, "%s" %client.receive())

filename = sys.argv[1]
with open(filename, "wb") as file:
    log(DEBUG, "serialized %s" %client)
    pickle.dump(client, file)      # serialize to file

###################################################
#
#     $ clientsave.py sclient
#     Client: localhost 2500 connected...
#     Server: received Here's a message
#     Server: sent HERE'S A MESSAGE
#     Client: HERE'S A MESSAGE
#     Client: serialized localhost 2500
#     Client: __getstate__() connection
#
