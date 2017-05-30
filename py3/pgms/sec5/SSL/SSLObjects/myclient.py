#!/usr/bin/env python3
# myclient.py - client objects
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)

client = Client(address, "mycert")     # Client object
if client.connect():
    log(DEBUG, "%s connected..." %client)
    message = "Message from secure socket"
    log(DEBUG, "sending %s" %message)
    client.send(message)

###################################################
#
#     $ myclient.py
#     Client: localhost 2500 connected...
#     Client: sending Message from secure socket
#     Server: received Message from secure socket
#
