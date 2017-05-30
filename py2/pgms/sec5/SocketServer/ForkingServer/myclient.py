#!/usr/bin/env python
# myclient.py - client objects
import sys
from Client import Client
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

if (len(sys.argv) == 1):
    raise SystemExit("Usage: %s cmd [args]" %sys.argv[0])

HOST = "localhost"
PORT = 2500
address = (HOST, PORT)

client = Client(address)
log(DEBUG, "%s connected..." %client)

cmd = " ".join(sys.argv[1:])
log(DEBUG, "sending '%s'" %cmd)
client.send(cmd + "\n")
output = client.receive()
log(DEBUG, "received %s" %output)

###################################################
#
#     $ myclient.py date
#     Client: localhost 2500 connected...
#     Client: sending 'date'
#     Server: received 'date'
#     Server: process 5023 sent Wed Jan  4 18:09:54 PST 2017
#     Client: received Wed Jan  4 18:09:54 PST 2017
#
