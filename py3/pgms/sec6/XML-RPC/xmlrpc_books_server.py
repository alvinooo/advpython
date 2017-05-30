#!/usr/bin/env python3
# xmlrpc_books_server.py - server to provide book catalog info
#
from xmlrpc.server import SimpleXMLRPCServer
import logging
import sqlite3

# set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer(('localhost', 9000),
                            logRequests=True,
                            allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()

class BookService:
    def get_books(self):
        """Returns the list of books as a dictionary sorted by
        author's last name. Dictionary keys include "id", "author",
        "title", "notes", and "copies".
        """

        logging.debug('BookService: %s', "calling get_books")
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.execute("SELECT * FROM BookCatalog order by author") 

        books = []
        for (id, author, title, notes, copies) in cursor:
            book = { "id": id,
                    "author": author,
                    "title": title,
                    "notes": notes,
                    "copies": copies }
            logging.debug('BookService: %s', book)
            books.append(book)
        conn.close()
        return books

server.register_instance(BookService())

try:
    print ('Starting server, use <CTRL-C> to stop')
    server.serve_forever()
except KeyboardInterrupt:
    print ('\nExiting . . . ')

