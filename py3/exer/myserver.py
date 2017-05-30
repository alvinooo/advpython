#!/usr/bin/env python3
# myserver.py - writable closures 

def serverState(newstate):
    # your code here...

server = serverState("off")
print "server is %s" %server()
server("up")
print "server is %s" %server()
server("down")
print "server is %s" %server()

#####################################
#
#     $ myserver.py
#     server is off
#     server is up
#     server is down
#      
