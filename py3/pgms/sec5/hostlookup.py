#!/usr/bin/env python3
# hostlookup.py - look up hosts
import socket

print("hostname:", socket.gethostname())

for host in ["python.org", "teradata.com", "twitter.com"]:
    print(host)
    try:
        (hostname, aliases, addr) = \
            socket.gethostbyname_ex(host)
        print("\thostname:", hostname)
        print("\taliases:", aliases)
        print("\taddresses:", addr)
    except socket.error as msg:
        raise SystemExit("%s" %msg)

#####################################
#
#     $ hostlookup.py
#     hostname: paul-VirtualBox
#     python.org
#         hostname: python.org
#         aliases: []
#         addresses: ['23.253.135.79']
#     teradata.com
#         hostname: teradata.com
#         aliases: []
#         addresses: ['153.65.20.219']
#     twitter.com
#         hostname: twitter.com
#         aliases: []
#         addresses: ['104.244.42.1', '104.244.42.193']
#
