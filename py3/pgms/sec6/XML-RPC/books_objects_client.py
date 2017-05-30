#!/usr/bin/env python3
# books_objects_client.py - show a sample client that uses XML-RPC protocol
# Create book objects
#           
import xmlrpc.client
from Book import Book
# if the verbose flag is True, XML output is 
# returned by the Server.
# server = xmlrpc.client.ServerProxy("http://localhost:9000", verbose=True)
server = xmlrpc.client.ServerProxy("http://localhost:9000")

# get list of books:
print ("Books: ")
books = server.get_books()
# sorted keys are in this order:
# author, copies, id, notes, title
# 0,      1,      2,  3,     4
#
# use keyword arguments and put arguments in
# sorted order

print("Keys unsorted: ", books[0].keys())
print("Keys sorted: ", sorted(books[0].keys()))

for b in books:
    sorted_keys = sorted(b.keys())
    book = Book(
        author=b[sorted_keys[0]],           #   b["author"], 
        copies=b[sorted_keys[1]],           #   b["copies"]
        id=b[sorted_keys[2]],               #   b["id"], 
        notes=b[sorted_keys[3]],            #   b["notes"], 
        title=b[sorted_keys[4]])            #   b["title"], 
    print(book)
print()

print("Authors: ")
authors = server.get_authors()
for author in authors:
    print(author)
print()

print("Titles: ")
titles = server.get_titles()
for title in titles:
    print(title)
print()

#################################################
#
#    $ books_objects_client.py
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
