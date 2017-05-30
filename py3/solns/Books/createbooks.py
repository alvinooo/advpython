#!/usr/bin/env python3
# createbooks.py - create book database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
conn.executescript("""
    DROP TABLE IF EXISTS BookCatalog;
    CREATE TABLE BookCatalog(
        id INTEGER NOT NULL PRIMARY KEY,
        author TEXT,
        title TEXT,
        notes CHAR(60),
        copies INTEGER);
    """)

cursor = conn.cursor()
cursor.execute("""SELECT name FROM sqlite_master 
                    WHERE type = 'table'""")

for (name,) in cursor:
    print(name, "created")
conn.close()

#################################################
#
#    $ createbooks.py
#    BookCatalog created
# 
