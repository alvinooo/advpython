#!/usr/bin/env python
# books_multicall_client.py - show a sample client that uses XML-RPC protocol
# with multicall option
#           
import xmlrpclib
# if the verbose flag is True, XML output is 
# returned by the Server.
#server = xmlrpclib.ServerProxy("http://localhost:9000", verbose=True)
server = xmlrpclib.ServerProxy("http://localhost:9000")

multicall = xmlrpclib.MultiCall(server)
multicall.get_books()
multicall.get_authors()
multicall.get_titles()

for i, results in enumerate(multicall()):
    if i == 0:
       print "Books "
       for book in results:
            print book["id"], book["author"], book["title"], book["copies"]
       print
    elif i == 1:
        print "Authors "
        for author in results:
            print author
        print 
    else:
        print "Titles "
        for title in results:
            print title
        print 

