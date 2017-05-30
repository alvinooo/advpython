#!/usr/bin/env python3
# totalbooks.py - book total in database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
total = sum([books for (books,) in
    conn.execute("SELECT copies FROM BookCatalog")])
print("total number of books = ", total)
conn.close()

#################################################
#
#    $ totalbooks.py
#    total number of books =  7
# 
