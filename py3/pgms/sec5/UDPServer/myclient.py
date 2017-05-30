#!/usr/bin/env python3
# myclient.py - UDP client
import sys, ast
from socket import *
from logging import *
basicConfig(level=ERROR, format="Client: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024

def show(data):
    if data.startswith("SQLError"):
        sys.stderr.write("%s\n" %data)
        return
    mylist = ast.literal_eval(data)
    log(DEBUG, mylist)
    for row in mylist:
        for col in row:
            print(col, end=' ')
        print()

sock = socket(AF_INET, SOCK_DGRAM)
address = (HOST, PORT)
log(DEBUG, "%s %d connected..." %address)

sql = "Select * from BookCatalog"
#sql = "Select title, copies from BookCatalog"

try:
    log(DEBUG, sql)
    sock.sendto(sql.encode("ascii"), address)
    (output, server) = sock.recvfrom(MAXDATA)
    show(output.decode("ascii"))
finally:
    sock.close()

#####################################
#
#     $ myclient.py
#     101 Hugo, Victor Les Miserables Classic 1
#     102 Crichton, Michael Jurassic Park Science Fiction 3
#     103 Grisham, John The Firm Fiction 2
#     104 Buffett, Jimmy Tales From Margaritaville Autobiography 1
#
