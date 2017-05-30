#!/usr/bin/env python3
# socketpair.py - UDS socket, parent and child
import os, socket

(parent, child) = socket.socketpair()
pid = os.fork()

if pid:              # Parent process
   child.close()
   parent.sendall("Here's a message.".encode("ascii"))
   message = parent.recv(1024)
   print("Child: %s" %message.decode("ascii"))
   parent.close()
else:                # Child process
   parent.close()
   message = child.recv(1024)
   print("Parent: %s" %message.decode("ascii"))
   child.sendall("Got it.".encode("ascii"))
   child.close()
    
#####################################
#
#     $ socketpair.py
#     Parent: Here's a message.
#     Child: Got it.
#
