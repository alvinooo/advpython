#!/usr/bin/env python3
# namedparms.py - select copies, named parameters
import sqlite3

ncopies = 1
conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("""
    SELECT title FROM BookCatalog
       WHERE copies = :ncopies 
    """, {"ncopies":ncopies}) 
for (title,) in cursor:
    print(title)
conn.close()

#################################################
#
#    $ namedparms.py
#    Les Miserables
#    Tales From Margaritaville
# 
