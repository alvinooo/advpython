#!/usr/bin/env python
# books_client.py - show a sample client that uses XML-RPC protocol
#           
import xmlrpclib
# if the verbose flag is True, XML output is 
# returned by the Server.
server = xmlrpclib.ServerProxy("http://localhost:9000", verbose=True)
# server = xmlrpclib.ServerProxy("http://localhost:9000")

# keys are sorted in this order
# author, copies, id, notes, title
# 0,      1,      2,  3,     4

# get list of books:
print "Books: "
books = server.get_books()
print books[0].keys()
for book in books:
    sorted_keys = sorted(book.keys())
    # id, author, title, notes, copies
    """
    print book[sorted_keys[2]],\
        book[sorted_keys[0]],\
        book[sorted_keys[4]],\
        book[sorted_keys[3]],\
        book[sorted_keys[1]]
    """
    print(book['id'], book['author'], book['title'], 
        book['notes'], book['copies'])
print

print "Authors: "
authors = server.get_authors()
for author in authors:
    print author
print 

print "Titles: "
titles = server.get_titles()
for title in titles:
    print title
print 

#################################################
#
#    $ books_client.py
# 
#    Books: 
#    104 Buffett, Jimmy Tales From Margaritaville 1
#    102 Crichton, Michael Jurassic Park 3
#    103 Grisham, John The Firm 2
#    101 Hugo, Victor Les Miserables 1
#    
#    Authors: 
#    Buffett, Jimmy
#    Crichton, Michael
#    Grisham, John
#    Hugo, Victor
#    
#    Titles: 
#    Jurassic Park
#    Les Miserables
#    Tales From Margaritaville
#    The Firm
