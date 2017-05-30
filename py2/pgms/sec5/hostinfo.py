#!/usr/bin/env python
# hostinfo.py - get host info
import sys, socket

if (len(sys.argv) < 3):
    raise SystemExit("Usage: %s host port" %sys.argv[0])

host = sys.argv[1]
port = sys.argv[2]

def getinfo(prefix):
    return dict((getattr(socket, name), name)
        for name in dir(socket)
            if name.startswith(prefix))

try:
    for info in socket.getaddrinfo(host, port, socket.AF_INET):
        (family, type, proto, name, addr) = info
        print "Family:", getinfo("AF_")[family]
        print "Type:", getinfo("SOCK_")[type]
        print "Protocol:", getinfo("IPPROTO_")[proto]
        print "Host: %s\nAddress, Port: %s\n" %(host, addr)
except socket.error as msg:
    raise SystemExit("%s" %msg)

#####################################
#
#     $ hostinfo.py python.org 80
#     Family: AF_INET
#     Type: SOCK_STREAM
#     Protocol: IPPROTO_TCP
#     Host: python.org
#     Address, Port: ('23.253.135.79', 80)
#
#     Family: AF_INET
#     Type: SOCK_DGRAM
#     Protocol: IPPROTO_UDP
#     Host: python.org
#     Address, Port: ('23.253.135.79', 80)
#
#     Family: AF_INET
#     Type: SOCK_RAW
#     Protocol: IPPROTO_IP
#     Host: python.org
#     Address, Port: ('23.253.135.79', 80)
#
