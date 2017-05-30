#!/usr/bin/env python
# cryptbooks.py - encrypt/decrypt book notes
import sqlite3

conn = sqlite3.connect("BookCatalog.db")
conn.create_function("encrypt", 1, lambda s : s.encode("rot-13"))
conn.create_function("decrypt", 1, lambda s : s.encode("rot-13"))

print "Encrypting..."
conn.execute("UPDATE BookCatalog SET notes = encrypt(notes)")
conn.commit()

cursor = conn.execute("SELECT title, notes FROM BookCatalog") 
for (title, notes) in cursor:
    print "%s: %s" %(title, notes)

print "Decrypting..."
cursor = conn.execute("""
    SELECT title, decrypt(notes) FROM BookCatalog
    """) 
for (title, notes) in cursor:
    print "%s: %s" %(title, notes)
conn.close()

#################################################
#
#    $ cryptbooks.py
#    Encrypting...
#    Les Miserables: Pynffvp
#    Jurassic Park: Fpvrapr Svpgvba
#    The Firm: Svpgvba
#    Tales From Margaritaville: Nhgbovbtencul
#    Decrypting...
#    Les Miserables: Classic
#    Jurassic Park: Science Fiction
#    The Firm: Fiction
#    Tales From Margaritaville: Autobiography
# 
