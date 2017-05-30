#!/usr/bin/env python
# importMusic.py - import Music sql database
import sqlite3, sys

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s filename" %sys.argv[0])

filename = sys.argv[1]
print "Importing Music database from", filename
file = open(filename, "r")
with file:
    data = file.read()

conn = sqlite3.connect("Music.db")
conn.executescript(data);
conn.close()

#################################################
#
#    $ importMusic.py Music.sql
#    Importing Music database from Music.sql
# 
