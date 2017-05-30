#!/usr/bin/env python
# myclient.py - client objects
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)

client = Client(address)     # Client object
log(DEBUG, "%s connected..." %client)

message = "Here's a message."
log(DEBUG, "sending %s" %message)
client.send(message)
data = client.receive()
log(DEBUG, "received %s" %data)

###################################################
#
#     $ myclient.py
#     Server: connection from 127.0.0.1 42754
#     Client: localhost 2500 connected...
#     Client: sending Here's a message.
#     Server: received Here's a message.
#     Server: sent HERE'S A MESSAGE.
#     Client: received HERE'S A MESSAGE.
#
