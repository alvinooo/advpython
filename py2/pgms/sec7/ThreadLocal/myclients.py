#!/usr/bin/env python
# myclients.py - client socket threads
from MyConnection import MyConnection
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024
data = "Here's a message."

def client(myconn):
    with myconn as sock:
        sock.send(data)
        debug("sent %s" %data)
        response = sock.recv(MAXDATA)
    debug("received %s" %response)
        
conn = MyConnection((HOST, PORT))

Thread(target=client, name="Client-1", args=(conn,)).start()
Thread(target=client, name="Client-2", args=(conn,)).start()

#####################################
#
#     $ myclients.py
#     Server: connection from 127.0.0.1 55561
#     (Client-1) sent Here's a message.
#     (Client-1) received HERE'S A MESSAGE.
#     Server: connection from 127.0.0.1 55562
#     (Client-2) sent Here's a message.
#     (Client-2) received HERE'S A MESSAGE.
#
