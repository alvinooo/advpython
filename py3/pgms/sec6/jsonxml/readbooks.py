#!/usr/bin/env python3
# readbooks.py - read books in database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("SELECT * FROM BookCatalog") 
for (id, author, title, notes, copies) in cursor:
    print(id, author, title, notes, copies)
conn.close()

#################################################
#
#    $ readbooks.py
#    101 Hugo, Victor Les Miserables Classic 1
#    102 Buffett, Jimmy Tales From Margaritaville Autobiography 1
# 
