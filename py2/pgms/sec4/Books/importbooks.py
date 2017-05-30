#!/usr/bin/env python
# importbooks.py - import book database
import sqlite3, sys

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

filename = sys.argv[1]
print "Importing BookCatalog from", filename
file = open(filename, "r")
with file:
    data = file.read()

conn = sqlite3.connect(":memory:")
conn.executescript(data);

cursor = conn.execute("SELECT * FROM BookCatalog") 
for (id, author, title, notes, copies) in cursor:
    print id, author, title, notes, copies
conn.close()

#################################################
#
#    $ importbooks.py Books.sql
#    Importing BookCatalog from Books.sql
#    101 Hugo, Victor Les Miserables Classic 1
#    102 Crichton, Michael Jurassic Park Science Fiction 3
#    103 Grisham, John The Firm Fiction 2
#    104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
# 
