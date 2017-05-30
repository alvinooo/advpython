#!/usr/bin/env python3
# json1.py - read books in database
import json
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
conn.row_factory = sqlite3.Row        # use a dictionary cursor
cursor = conn.execute("SELECT * FROM BookCatalog order by author") 
books = cursor.fetchall()

book_list = [dict(book) for book in books]
print("Convert dict with embedded list to JSON str:")
jstr = json.dumps({'books': book_list })
print(jstr)

# Convert back to python objects
books = json.loads(jstr)
for book in books['books']:
    print("%s %s %d" %(book['title'], book['author'], book['copies']))
conn.close()

#######################################################
#
#   $ json1.py
#   Convert dict with embedded list to JSON str:
#   {"books": [{"copies": 1, "notes": "Autobiography", 
#   "title": "Tales From Margaritaville", "id": 102, 
#   "author": "Buffett, Jimmy"}, {"copies": 1, "notes": "Classic", 
#   "title": "Les Miserables", "id": 101, 
#   "author": "Hugo, Victor"}]}
#   Tales From Margaritaville Buffett, Jimmy 1
#   Les Miserables Hugo, Victor 1
