#!/usr/bin/env python3
# myclient.py - client objects
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)

client = Client(address)
log(DEBUG, "%s %d connected..." %address)

message = "Here's a message."
log(DEBUG, "sending %s" %message)
client.send(message + "\n")
data = client.receive()
log(DEBUG, "received %s" %data)

###################################################
#
#     $ myclient.py
#     Client: localhost 2500 connected...
#     Client: sending Here's a message.
#     Server: received b"Here's a message."
#     Server: sent b"HERE'S A MESSAGE."
#     Client: received HERE'S A MESSAGE.
#
