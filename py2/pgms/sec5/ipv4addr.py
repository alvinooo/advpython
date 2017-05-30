#!/usr/bin/env python
# ipv4addr.py - IPv4 address functions
import socket, binascii

for host in ["python.org", "teradata.com"]:
    print host
    try:
        address = socket.gethostbyname(host)
        print "\taddress:", address
        packed = socket.inet_aton(address)
        print "\tpacked:", binascii.hexlify(packed)
        unpacked = socket.inet_ntoa(packed)
        print "\tunpacked:", unpacked
    except socket.error as msg:
        raise SystemExit("%s" %msg)

#####################################
#
#     $ ipv4addr.py
#     python.org
#         address: 23.253.135.79
#         packed: 17fd874f
#         unpacked: 23.253.135.79
#     teradata.com
#         address: 153.65.20.219
#         packed: 994114db
#         unpacked: 153.65.20.219
#
