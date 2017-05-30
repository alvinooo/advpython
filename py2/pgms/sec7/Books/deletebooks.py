#!/usr/bin/env python
# deletebooks.py - atomic delete books from database
import sqlite3
from threading import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

deleteLock = Lock()       # lock deletes to database

def deletebook(title):
    conn = sqlite3.connect("BookCatalog.db")
    with deleteLock:
        debug("lock delete")
        with conn:
            debug("delete %s" %title)
            cursor = conn.execute("""
                SELECT copies FROM BookCatalog
                    WHERE title = ?""", (title,))
            row = cursor.fetchone()
            if row: 
                ncopies = row[0]
                if ncopies == 1:
                    conn.execute("""
                        DELETE FROM BookCatalog 
                            WHERE title = ?""", (title,))
                else:
                    debug("%s: copies now = %d" %(title, ncopies-1))
                    conn.execute("""
                        UPDATE BookCatalog SET copies = copies-1
                            WHERE title = ?""", (title,))
                conn.commit()
            else:
                debug("%s not found" %title)
    debug("unlock delete")

books = [("Jurassic Park",), ("Les Miserables",)]

for num in range(2):
    thread = Thread(target=deletebook, args=books[num])
    thread.start()

mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        thread.join()
debug("done")

#################################################
#
#    $ deletebooks.py
#    (Thread-1) lock delete
#    (Thread-1) delete Jurassic Park
#    (Thread-1) Jurassic Park: copies now = 2
#    (Thread-1) unlock delete
#    (Thread-2) lock delete
#    (Thread-2) delete Les Miserables
#    (Thread-2) unlock delete
#    (MainThread) done
#  
