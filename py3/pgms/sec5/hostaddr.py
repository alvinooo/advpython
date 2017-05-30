#!/usr/bin/env python3
# hostaddr.py - get host from address
import sys, socket

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s address" %sys.argv[0])

address = sys.argv[1]

try:
    (hostname, aliases, addr) = socket.gethostbyaddr(address)
    print("hostname:", hostname)
    print("aliases:", aliases)
    print("addresses:", addr)
except socket.error as msg:
    raise SystemExit("%s" %msg)

#####################################
#
#     $ hostaddr.py '153.65.20.219'
#     hostname: teradata.jp
#     aliases: []
#     addresses: ['153.65.20.219']
#
#     $ hostaddr.py '129.42.38.1'
#     hostname: redirect.www.ibm.com
#     aliases: []
#     addresses: ['129.42.38.1']
#
