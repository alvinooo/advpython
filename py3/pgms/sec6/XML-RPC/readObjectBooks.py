#!/usr/bin/env python3
# readObjectBooks.py - read books in database
import sqlite3
from Book import Book

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("SELECT * FROM BookCatalog") 
        
books = [ Book(id, author, title, notes, copies)
        for (id, author, title, notes, copies) in cursor]

conn.close()

for book in books:
    print(book)

for book in books:
    print(book.author)

#################################################
#
#    $ readObjectBooks.py
#    101 Hugo, Victor Les Miserables Classic 1
#    102 Crichton, Michael Jurassic Park Science Fiction 3
#    103 Grisham, John The Firm Fiction 2
#    104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
#    Hugo, Victor
#    Crichton, Michael
#    Grisham, John
#    Buffett, Jimmy
