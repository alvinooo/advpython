#!/usr/bin/env python3
# myserver3.py - writable closures, nonlocal

def serverState(newstate):
    state = newstate
    def update(newst=None):
        nonlocal state
        if newst != None:
            state = newst
        return state
    return update

server = serverState("off")
print(("server is %s" %server()))
server("up")
print(("server is %s" %server()))
server("down")
print(("server is %s" %server()))

#####################################
#
#     $ myserver3.py
#     server is off
#     server is up
#     server is down
#      
