#!/usr/bin/env python
# rollback.py - rollback book transaction
import sqlite3, sys

def showBooks(conn):
    cursor = conn.execute("""
        SELECT author, title FROM BookCatalog
    """) 
    for (author, title) in cursor:
        print "%s: %s" %(author, title)
    print

try:
    conn = sqlite3.connect("BookCatalog.db")
    showBooks(conn)
    conn.execute("""
        DELETE FROM BookCatalog WHERE title = 'The Firm'
    """)
    showBooks(conn)
    raise RuntimeError("some problem...")

except Exception as ex:
    sys.stderr.write("Error: %s\n" %ex)
    conn.rollback()
    print "rollback"
else:
    conn.commit()
    print "commit"

showBooks(conn)
conn.close()

#################################################
#
#    $ rollback.py
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Grisham, John: The Firm
#    Buffett, Jimmy: Tales From Margaritaville
#    
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Buffett, Jimmy: Tales From Margaritaville
#    
#    Error: some problem...
#    rollback
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Grisham, John: The Firm
#    Buffett, Jimmy: Tales From Margaritaville
# 
#    (comment out raise RuntimeError, so no error)
#    $ rollback.py
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Grisham, John: The Firm
#    Buffett, Jimmy: Tales From Margaritaville
#    
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Buffett, Jimmy: Tales From Margaritaville
#    
#    commit
#    Hugo, Victor: Les Miserables
#    Crichton, Michael: Jurassic Park
#    Buffett, Jimmy: Tales From Margaritaville
#    
