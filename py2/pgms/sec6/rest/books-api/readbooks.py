#!/usr/bin/env python
# readbooks.py - read books in database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("SELECT * FROM BookCatalog") 
for (id, author, title, notes, copies) in cursor:
    print id, author, title, notes, copies
conn.close()

#################################################
#
#    $ readbooks.py
#    101 Hugo, Victor Les Miserables Classic 1
#    102 Crichton, Michael Jurassic Park Science Fiction 3
#    103 Grisham, John The Firm Fiction 2
#    104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
# 
