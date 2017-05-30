#!/usr/bin/env python3
# deletebooks.py - delete books from database
import sqlite3

def deletebook(title):
    # your code here...

conn = sqlite3.connect("BookCatalog.db")
deletebook("Les Miserables")
deletebook("Jurassic Park")
conn.close()

#################################################
#
#    $ deletebooks.py
#    deleting Les Miserables
#    Jurassic Park: copies now = 2
# 
#    $ deletebooks.py
#    Les Miserables not found
#    Jurassic Park: copies now = 1
#
#    $ deletebooks.py
#    Les Miserables not found
#    deleting Jurassic Park
#
#    $ deletebooks.py
#    Les Miserables not found
#    Jurassic Park not found
#
#    $ readbooks.py
#    103 Grisham, John The Firm Fiction 2
#    104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
#  
