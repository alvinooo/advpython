#!/usr/bin/env python3
# books_introspection_client.py - show a client that displays 
# introspection information from the books_server Server
#           
import xmlrpc.client
# if the verbose flag is True, XML output is 
# returned by the Server.
#server = xmlrpc.client.ServerProxy("http://localhost:9000", verbose=True)
server = xmlrpc.client.ServerProxy("http://localhost:9000")

for method_name in server.system.listMethods():
    print (method_name)
    print()
    print (server.system.methodHelp(method_name))
    print ('-' * 30)
