#!/usr/bin/env python3
# sendbinary.py - send TCP binary data
import binascii
from socket import *
from subprocess import check_output
from struct import *
from logging import *
basicConfig(level=DEBUG, format="Sender: %(message)s",)

HOST = "localhost"
PORT = 2500

sock = socket(AF_INET, SOCK_STREAM)
address = (HOST, PORT)
sock.connect(address)
log(DEBUG, "%s %d connected..." %address)

now = check_output("date", shell=True).strip()
data = (500, now, 3.45)
log(DEBUG, data)

packer = Struct("i 28s f")
log(DEBUG, "packing format: %s" %packer.format)
packdata = packer.pack(*data)
hexdata = binascii.hexlify(packdata)
 
try:
    log(DEBUG, hexdata)
    sock.sendall(packdata)
finally:
    sock.close()

###################################################
#
#     $ sendbinary.py
#     Receiver: connection from 127.0.0.1 42725
#     Sender: localhost 2500 connected...
#     Sender: (500, b'Sat Jan  7 10:07:15 PST 2017', 3.45)
#     Sender: packing format: b'i 28s f'
#     Sender: b'f4010000536174204a616e2020372031303a30373a31352050
#     53542032303137cdcc5c40'
#     Receiver: b'f4010000536174204a616e2020372031303a30373a31352050
#     53542032303137cdcc5c40'
#     Receiver: (500, b'Sat Jan  7 10:07:15 PST 2017', 3.450000047683716
#
