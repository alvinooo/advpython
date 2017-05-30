#!/usr/bin/env python3
# metadata.py - metadata with books
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
cursor = conn.execute("PRAGMA table_info(BookCatalog)") 
metadata = cursor.fetchall()
for col in metadata:
    print(col[0], col[1], col[2])

cursor = conn.execute("""SELECT name FROM sqlite_master 
                    WHERE type = 'table'""")
print("%35s" %cursor.fetchone()[0])   # database name

cursor = conn.execute("""
    SELECT id, author, title FROM BookCatalog""")
names = [name[0].lower() for name in cursor.description]
print("%-5s %15s %25s" %(names[0], names[1], names[2]))

for (id, author, title) in cursor:
    print("%-10s %-25s %-20s" %(id, author, title))
conn.close()

#################################################
#
#    $ metadata.py
#    0 id INTEGER
#    1 author TEXT
#    2 title TEXT
#    3 notes CHAR(60)
#    4 copies INTEGER
#                            BookCatalog
#    id             author                     title
#    101        Hugo, Victor              Les Miserables      
#    102        Crichton, Michael         Jurassic Park       
#    103        Grisham, John             The Firm            
#    104        Buffett, Jimmy            Tales From Margaritaville
# 
