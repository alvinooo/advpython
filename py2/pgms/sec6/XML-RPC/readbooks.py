#!/usr/bin/env python
# readbooks.py - read books in database
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("SELECT * FROM BookCatalog") 
for (id, author, title, notes, copies) in cursor:
    print id, author, title, notes, copies
conn.close()

#################################################
#
#    $ readbooks.py
#    101 Hugo, Victor Les Miserables Literary Fiction 1
#    102 Crichton, Michael Jurassic Park Science Fiction 3
#    103 Grisham, John The Firm Fiction 2
#    104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
#    105 Zola, Emile The Masterpiece Literary Fiction 1
#    106 Zola, Emile Germinal Literary Fiction 1
#    107 Stewart, Rory The Places in Between Non-Fiction 1
#    108 Ceder, Naomi The Quick Python Book Computer Programming 1
#    109 Larsen, Stieg The Girl with the Dragon Tatoo Fiction 1
# 
