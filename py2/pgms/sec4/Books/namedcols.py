#!/usr/bin/env python
# namedcols.py - access named columns
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
conn.row_factory = sqlite3.Row
cursor = conn.execute("""
            SELECT title, copies, notes FROM BookCatalog
       """) 
for row in cursor:
    print row["title"], row["copies"], row["notes"]
conn.close()

#################################################
#
#    $ namedcols.py
#    Les Miserables 1 Classic
#    Jurassic Park 3 Science Fiction
#    The Firm 2 Fiction
#    Tales From Margaritaville 1 Autobiography
# 
