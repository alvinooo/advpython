#!/usr/bin/env python3
# bookmodule.py - totalbooks() function
import sqlite3

def totalbooks(dbase):
    if type(dbase) is str and dbase.endswith(".db"):
        print("Python: reading %s" %dbase)
        conn = sqlite3.connect(dbase)
        total = sum([books for (books,) in
            conn.execute("SELECT copies FROM " + dbase[:-3])])
        conn.close()
        return total
    raise TypeError("%s is not a database" %dbase)

if __name__ == "__main__":     # run as main program
    import sys
    if (len(sys.argv) < 2):
        raise SystemExit("Usage: %s BookCatalog.db" %sys.argv[0])

    dbname = sys.argv[1]
    print("Total number of books = %d" %totalbooks(dbname))

##########################################
#
#    $ bookmodule.py BookCatalog.db
#    Total number of books = 7
#
