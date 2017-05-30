#!/usr/bin/env python3
# myserver.py - TCP server
import sys, Books
from socket import *
from logging import *
basicConfig(level=ERROR, format="Server: %(message)s",)

HOST = "localhost"
PORT = 2500
MAXDATA = 1024

sock = socket(AF_INET, SOCK_STREAM)
address = (HOST, PORT)
sock.bind(address)
sock.listen(5)
conn = None

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        (conn, addr) = sock.accept()
        log(DEBUG, "connection from %s %d" %addr)
        sql = conn.recv(MAXDATA)
        log(DEBUG, sql)
        output = Books.run(sql.decode("ascii"))
        log(DEBUG, output)
        conn.sendall(output.encode("ascii"))
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)
finally:
    if conn is not None:
        conn.close()

#####################################
#
#     $ myserver.py
#
