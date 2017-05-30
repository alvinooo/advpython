#!/usr/bin/env python
# updatebooks2.py - update books in database, named params
import sqlite3

def increaseCopies(title, ncopies):
    print "Update %s for %d copies" %(title, ncopies)
    conn.execute("""
        UPDATE BookCatalog SET copies = copies + :ncopies
            WHERE title = :title""", 
                {"ncopies" : ncopies, "title" : title})
    conn.commit()
    
conn = sqlite3.connect("BookCatalog.db")
increaseCopies("Jurassic Park", 2)
increaseCopies("Les Miserables", 1)
conn.close()

#################################################
#
#    $ updatebooks2.py
#    Update Jurassic Park for 2 copies
#    Update Les Miserables for 1 copies
# 
