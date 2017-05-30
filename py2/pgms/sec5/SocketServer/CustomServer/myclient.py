#!/usr/bin/env python
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
#     Server: verfy_request 127.0.0.1 49427
#     Server: process_request 127.0.0.1 49427
#     Server: finish_request 127.0.0.1 49427
#     Server: handler setup
#     Client: localhost 2500 connected...
#     Client: sending Here's a message.
#     Server: handler received Here's a message.
#     Server: handler sent HERE'S A MESSAGE.
#     Server: handler finish
#     Server: close_request
#     Client: received HERE'S A MESSAGE.
#
