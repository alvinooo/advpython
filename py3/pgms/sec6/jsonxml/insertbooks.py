#!/usr/bin/env python3
# insertbooks.py - insert books into database
import sqlite3

books = ( (101, "Hugo, Victor", "Les Miserables", 
                "Classic", 1),
          (102, "Buffett, Jimmy", "Tales From Margaritaville",
                "Autobiography", 1)
        )

conn = sqlite3.connect("BookCatalog.db")
conn.executemany("""
    INSERT INTO BookCatalog(id, author, title, notes, copies) 
        VALUES (?,?,?,?,?)
    """, books)
conn.commit()               # commit to database

print(conn.total_changes, "books inserted in catalog")
conn.close()

#################################################
#
#    $ insertbooks.py
#    2 books inserted in catalog
# 
