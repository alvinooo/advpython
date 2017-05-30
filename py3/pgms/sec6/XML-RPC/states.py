#!/usr/bin/env python3
# states.py - show a sample client that uses XML-RPC protocol
#           
import xmlrpc.client
server = xmlrpc.client.ServerProxy("http://betty.userland.com/RPC2")

# get South Dakota
print(server.examples.getStateName(41))

# get Alabama
print(server.examples.getStateName(1))
print("-----")

# get all the states by getting the range 1-50
st = list(range(1, 50))

mystates = server.examples.getStateList(st)
print(mystates)
print()

# make the states into a list
states = mystates.split(",")
for state in states:
    print(state)
print("-----")


# get these states
st = [1, 3, 15, 22, 45 ]
print(server.examples.getStateList(st))

