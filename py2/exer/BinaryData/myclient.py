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
    # your code here...
    print "Client: sending filename {0}".format(infile)
    sock.send(infile)
    response = sock.recv(MAXDATA)
    print "Client: received {0} bytes".format(unpacker.unpack(response)[0])
    print "Client: writing file {0}".format(outfile)
    with open(outfile, "wb") as f:
        while True:
            data = sock.recv(MAXDATA)
            f.write(data)
            print "Client: {0} bytes".format(len(data))
            if len(data) < MAXDATA:
                break
    print "Client: done"

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
