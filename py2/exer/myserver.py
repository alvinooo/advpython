#!/usr/bin/env python
# myserver.py - writable closures

def serverState(newstate):
    # your code here...
    serverState.state = newstate
    def update(newst=None):
        if newst is None:
            serverState.state = newst
        return serverState.state
    return update

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
