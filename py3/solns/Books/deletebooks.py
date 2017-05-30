#!/usr/bin/env python3
# deletebooks.py - delete books from database
import sqlite3

def deletebook(title):
    cursor = conn.execute("""
        SELECT copies FROM BookCatalog
            WHERE title = ?""", (title,))
    row = cursor.fetchone()
    if row == None: 
        print(title, "not found")
        return
    ncopies = row[0]
    if ncopies == 1:
        print("deleting", title)
        conn.execute("""
            DELETE FROM BookCatalog 
                WHERE title = ?""", (title,))
    else:
        print("%s: copies now = %d" %(title, ncopies-1))
        conn.execute("""
            UPDATE BookCatalog SET copies = copies-1
                WHERE title = ?""", (title,))
    conn.commit()

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
