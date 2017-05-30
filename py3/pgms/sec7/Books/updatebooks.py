#!/usr/bin/env python3
# updatebooks.py - update books in database
import sqlite3

def increaseCopies(title, ncopies):
    print("Update %s for %d copies" %(title, ncopies))
    conn.execute("""
        UPDATE BookCatalog SET copies = copies+?
            WHERE title = ?""", (ncopies, title))
    conn.commit()
    
conn = sqlite3.connect("BookCatalog.db")
increaseCopies("Jurassic Park", 2)
increaseCopies("Les Miserables", 1)
conn.close()

#################################################
#
#    $ updatebooks.py
#    Update Jurassic Park for 2 copies
#    Update Les Miserables for 1 copies
# 
