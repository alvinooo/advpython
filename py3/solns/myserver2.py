#!/usr/bin/env python3
# myserver2.py - writable closures 

def serverState(newstate):
    state = [None]
    state[0] = newstate
    def update(newst=None):
        if newst != None:
            state[0] = newst
        return state[0]
    return update

server = serverState("off")
print("server is %s" %server())
server("up")
print("server is %s" %server())
server("down")
print("server is %s" %server())

#####################################
#
#     $ myserver2.py
#     server is off
#     server is up
#     server is down
#      
