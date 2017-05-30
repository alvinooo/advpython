#!/usr/bin/env python
# myserver.py - writable closures, function attributes

def serverState(newstate):
    serverState.state = newstate
    def update(newst=None):
        if newst != None:
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
