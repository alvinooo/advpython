#!/usr/bin/env python
# myclient.py - UDS client
import sys, ast
from socket import *
from logging import *
basicConfig(level=ERROR, format="Client: %(message)s",)

ADDR = "uds_socket"
MAXDATA = 1024

def show(data):
    if data.startswith("SQLError"):
        sys.stderr.write("%s\n" %data)
        return
    mylist = ast.literal_eval(data)
    log(DEBUG, mylist)
    for row in mylist:
        for col in row:
            print col,
        print

sock = socket(AF_UNIX, SOCK_STREAM)
sock.connect(ADDR)
log(DEBUG, "%s connected..." %ADDR)

sql = "Select * from BookCatalog"
#sql = "Select title, copies from BookCatalog"

try:
    log(DEBUG, sql)
    sock.sendall(sql)
    output = sock.recv(MAXDATA)
    show(output)
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
