#!/usr/bin/env python
# readbooksTest.py - read books in database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.cursor()
cursor.execute('PRAGMA TABLE_INFO({})'.format('BookCatalog'))

# collect names in a list
column_names = [tup[1] for tup in cursor.fetchall()]
# print(column_names)
cursor = conn.execute("SELECT * FROM BookCatalog") 
books = cursor.fetchall()

book_list = [ dict(zip(column_names, b)) for b in books ]
print ("new book list:")
for book in book_list:
    print book
conn.close()

