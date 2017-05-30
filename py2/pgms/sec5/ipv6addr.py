#!/usr/bin/env python
# ipv6addr.py - IPv6 address functions
import socket, binascii

if socket.has_ipv6: print "Ipv6 supported"

try:
    info = socket.getaddrinfo("python.org", 
                        80, 0, 0, socket.SOL_TCP)
    print info[1]
    address = info[1][4][0]
    print "\taddress:", address
    packed = socket.inet_pton(socket.AF_INET6, address)
    print "\tpacked:", binascii.hexlify(packed)
    unpacked = socket.inet_ntop(socket.AF_INET6, packed)
    print "\tunpacked:", unpacked
except socket.error as msg:
    raise SystemExit("%s" %msg)

######################################################
#
#     $ ipv6addr.py
#     Ipv6 supported
#     (10, 1, 6, '', ('2001:4802:7901:0:e60a:1375:0:6', 80, 0, 0))
#         address: 2001:4802:7901:0:e60a:1375:0:6
#         packed: 2001480279010000e60a137500000006
#         unpacked: 2001:4802:7901:0:e60a:1375:0:6
#
