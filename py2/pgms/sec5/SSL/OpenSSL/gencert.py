#!/usr/bin/env python
# gencert.py - generate certificate for ssl
from subprocess import call

cmd = "openssl req -new -x509 -nodes \
          -sha1 -days 365 -key key > cert"
retval = call(cmd, shell=True)

#################################################
#
#    $ gencert.py
#    You are about to be asked to enter information that
#    will be incorporated into your certificate request.
#    -----
#    Country Name (2 letter code) [AU]:US
#    State or Province Name (full name) [Some-State]:California
#    Locality Name (eg, city) []:San Diego
#    Organization Name (eg, company) [Internet Widgits Pty Ltd]:ASG
#    Organizational Unit Name (eg, section) []:.
#    Common Name (e.g. server FQDN or YOUR name) []:Paul
#    Email Address []:.
#    $
# 
