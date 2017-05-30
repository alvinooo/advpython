#!/usr/bin/env python
# exportbooks.py - export book database
import sqlite3, sys

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

conn = sqlite3.connect(":memory:")
conn.executescript("""
    DROP TABLE IF EXISTS BookCatalog;
    CREATE TABLE BookCatalog(
        id INTEGER NOT NULL PRIMARY KEY,
        author TEXT,
        title TEXT,
        notes CHAR(60),
        copies INTEGER);
    """)

books = ( (101, "Hugo, Victor", "Les Miserables", 
                "Classic", 1),
          (102, "Crichton, Michael", "Jurassic Park",
                "Science Fiction", 3),
          (103, "Grisham, John", "The Firm",
                "Fiction", 2),
          (104, "Buffett, Jimmy", "Tales From Margaritaville",
                "Autobiography", 1)
        )

conn.executemany("""
    INSERT INTO BookCatalog(id, author, title, notes, copies) 
        VALUES (?,?,?,?,?)
    """, books)

filename = sys.argv[1]
print "Exporting BookCatalog to", filename
file = open(filename, "w")
with file:
    for text in conn.iterdump():
        file.write("%s\n" %text)
conn.close()

#################################################
#
#    $ exportbooks.py Books.sql
#    Exporting BookCatalog to Books.sql
# 
