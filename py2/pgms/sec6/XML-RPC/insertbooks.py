#!/usr/bin/env python
# insertbooks.py - insert books into database
import sqlite3

books = ( (101, "Hugo, Victor", "Les Miserables", 
                "Literary Fiction", 1),
          (102, "Crichton, Michael", "Jurassic Park",
                "Science Fiction", 3),
          (103, "Grisham, John", "The Firm",
                "Fiction", 2),
          (104, "Buffett, Jimmy", "Tales From Margaritaville",
                "Autobiography", 1),
          (105, "Zola, Emile", "The Masterpiece",
                "Literary Fiction", 1),
          (106, "Zola, Emile", "Germinal",
                "Literary Fiction", 1),
          (107, "Stewart, Rory", "The Places in Between",
                "Non-Fiction", 1),
          (108, "Ceder, Naomi", "The Quick Python Book",
                "Computer Programming", 1),
          (109, "Larsen, Stieg", "The Girl with the Dragon Tatoo",
                "Fiction", 1)
        )

conn = sqlite3.connect("BookCatalog.db")
conn.executemany("""
    INSERT INTO BookCatalog(id, author, title, notes, copies) 
        VALUES (?,?,?,?,?)
    """, books)
conn.commit()               # commit to database

print conn.total_changes, "books inserted in catalog"
conn.close()

#################################################
#
#    $ insertbooks.py
#    9 books inserted in catalog
# 
