# Books.py - Books database module
import sqlite3

def run(sql):
    try:
        conn = sqlite3.connect("BookCatalog.db")
        cursor = conn.execute(sql)
        output = str(cursor.fetchall())
        conn.close()
        return output
    except sqlite3.DatabaseError as ex:
        return "SQLError - %s" %ex
