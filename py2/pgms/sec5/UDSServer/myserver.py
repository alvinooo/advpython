#!/usr/bin/env python
# myserver.py - UDS server
import os, sys, Books
from socket import *
from logging import *
basicConfig(level=ERROR, format="Server: %(message)s",)

ADDR = "uds_socket"
MAXDATA = 1024
if os.path.exists(ADDR): os.remove(ADDR)

sock = socket(AF_UNIX, SOCK_STREAM)
sock.bind(ADDR)
sock.listen(5)
conn = None

log(DEBUG, "%s running..." %ADDR)
try:
    while True:
        (conn, addr) = sock.accept()
        log(DEBUG, "connection from %s" %addr)
        sql = conn.recv(MAXDATA)
        log(DEBUG, sql)
        output = Books.run(sql)
        log(DEBUG, output)
        conn.sendall(output)
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
