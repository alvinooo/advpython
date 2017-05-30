#!/usr/bin/env python3
# myserver.py - TCP SSL server
import sys, ssl
from socket import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

HOST = "localhost"; PORT = 2500

sock = socket(AF_INET, SOCK_STREAM)
address = (HOST, PORT)
sock.bind(address); sock.listen(5)
conn = sslSocket = None

log(DEBUG, "%s %d running..." %address)
try:
    while True:
        (conn, addr) = sock.accept()
        log(DEBUG, "connection from %s %d" %addr)
        try:
            sslSocket = ssl.wrap_socket(conn,
                server_side = True, certfile = "mycert")
            data = sslSocket.read().decode("ascii")
            log(DEBUG, "received %s" %data)
        except ssl.SSLError as ex:
            msg = str(ex)
            log(DEBUG, "%s" %msg[msg.find(": ")+2:])
            conn.close()
except KeyboardInterrupt:
    log(DEBUG, "stopped")
    sys.exit(1)
finally:
    if conn is not None:
        conn.close()
    if sslSocket is not None:
        sslSocket.close()

#####################################
#
#     $ myserver.py
#     Server: localhost 2500 running...
#
#     ^C
#     Server: stopped
#     $
#
