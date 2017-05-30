#!/usr/bin/env python
# myclient.py - TCP client, binary data
import sys, socket
from struct import *
from logging import *
basicConfig(level=DEBUG, format="Client: %(message)s",)

if (len(sys.argv) < 3):
    raise SystemExit("Usage: %s infile outfile" %sys.argv[0])

HOST = "localhost"
PORT = 2500
MAXDATA = 4096

infile = sys.argv[1]
outfile = sys.argv[2]
file = open(outfile, "wb+")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (HOST, PORT)
sock.connect(address)
log(DEBUG, "%s %d connected..." %address)

unpacker = Struct("I")       # file length integer
psize = unpacker.size        # pack size
log(DEBUG, "unpacking format: %s" %unpacker.format)

try:
    log(DEBUG, "sending filename %s" %infile)
    sock.sendall(infile)
    pdata = sock.recv(psize)
    filelength = unpacker.unpack(pdata)[0]
    log(DEBUG, "received %d bytes" %filelength)
    bytes = 0
    log(DEBUG, "writing file %s" %outfile)
    while bytes < filelength:
        data = sock.recv(MAXDATA)
        file.write(data)
        log(DEBUG, "%d bytes" %len(data))
        bytes += len(data)
    log(DEBUG, "done")
finally:
    file.close()
    sock.close()

#####################################
#
#     $ myclient.py photo.jpg myphoto.jpg
#     Client: localhost 2500 connected...
#     Client: unpacking format: I
#     Client: sending filename photo.jpg
#     Server: received filename photo.jpg:
#     Server: sending file length 144638:
#     Server: sending 144638 bytes
#     Client: received 144638 bytes
#     Client: writing file myphoto.jpg
#     Client: 4096 bytes
#     Client: 4096 bytes
#     Client: 4096 bytes
#     . . .
#     Client: 1278 bytes
#     Client: done
#
