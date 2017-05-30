#!/usr/bin/env python
# xmlrpc_books_client.py - show a sample client that uses XML-RPC protocol
#           
import xmlrpclib
# if the verbose flag is True, XML output is 
# returned by the Server.
# server = xmlrpclib.ServerProxy("http://localhost:9000", verbose=True)
server = xmlrpclib.ServerProxy("http://localhost:9000")

# get list of books:
print "Books: "
books = server.get_books()
for book in books:
    print("%s\t\t%s\n%s\n%s\t%d\n" %(book['id'], book['author'], 
        book['title'], book['notes'], book['copies']))

#################################################
#
#    $ xmlrpc_books_client.py
#    Books: 
#    104		Buffett, Jimmy
#    Tales From Margaritaville
#    Autobiography	1
#    
#    102		Crichton, Michael
#    Jurassic Park
#    Science Fiction	3
#    
#    103		Grisham, John
#    The Firm
#    Fiction	2
#    
#    101		Hugo, Victor
#    Les Miserables
#    Classic	1
#    
