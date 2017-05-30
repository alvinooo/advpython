#!/usr/bin/env python
# books_server.py - server to provide book catalog info
#
from SimpleXMLRPCServer import SimpleXMLRPCServer
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

    def __get_field(self, field):
        logging.debug('get_field for %s', field)
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.execute("SELECT " + 
                field + " FROM BookCatalog order by " + field) 

        answers = []
        for f in cursor:
            # f is a tuple, but only f[0] is in range
            answers.append(f[0])
            logging.debug('BookService: %s', f[0])
        conn.close()
        return answers

    def get_authors(self):
        """Returns the list of authors sorted by
        author's last name.
        """
        logging.debug('BookService: %s', "calling get_authors")
        return self.__get_field("author")

    def get_titles(self):
        """Returns the list of titles sorted by
        title name.
        """
        logging.debug('BookService: %s', "calling get_titles")
        return self.__get_field("title")

server.register_instance(BookService())

try:
    print 'Starting server, use <CTRL-C> to stop'
    server.serve_forever()
except KeyboardInterrupt:
    print '\nExiting . . . '
