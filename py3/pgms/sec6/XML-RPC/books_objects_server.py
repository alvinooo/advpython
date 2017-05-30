#!/usr/bin/env python3
# books_objects_server.py - server to provide book catalog info
# Book is a class
#
from xmlrpc.server import SimpleXMLRPCServer
# from xmlrpc.server import Binary
import logging
import sqlite3
from Book import Book

# set up logging
logging.basicConfig(level=logging.ERROR)

server = SimpleXMLRPCServer(('localhost', 9000),
                            logRequests=True,
                            allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()

class BookService:
    def get_books(self):
        """Returns the list of books as a dictionary sorted by
        author's last name. Dictionary keys are from Book's __dict__.
        """

        logging.debug('BookService: %s', "calling get_books")
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.execute("SELECT * FROM BookCatalog order by author") 

        books = [ Book(id, author, title, notes, copies)
            for (id, author, title, notes, copies) in cursor]
        for book in books:
            logging.debug('BookService: %s', book.__dict__)

        conn.close()
        return books

    def __get_field(self, field):
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.execute("SELECT " + field 
                    + " FROM BookCatalog order by " + field) 

        answers = []
        for field in cursor:
            answers.append(field[0])
            logging.debug('BookService: %s', field[0])
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
    print ('Starting server, use <CTRL-C> to stop')
    server.serve_forever()
except KeyboardInterrupt:
    print ('\nExiting . . . ')
