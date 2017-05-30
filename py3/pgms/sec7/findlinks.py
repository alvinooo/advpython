#!/usr/bin/env python3
# findlinks.py - find url links
import sys
import urllib.request, urllib.error, urllib.parse
import re

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s url" %sys.argv[0])
url = sys.argv[1]

website = urllib.request.urlopen("http://%s" %url)
html = website.read()
regex = '"((http|ftp)s?://.*?)"'.encode("ascii")
links = re.findall(regex, html)
for link in links:
    print(link[0])

###########################################################
#
#     $ findlinks.py google.com
#     http://schema.org/WebPage
#     http://www.google.com/imghp?hl=en&tab=wi
#     http://maps.google.com/maps?hl=en&tab=wl
#     https://play.google.com/?hl=en&tab=w8
#     http://www.youtube.com/?tab=w1
#     http://news.google.com/nwshp?hl=en&tab=wn
#     https://mail.google.com/mail/?tab=wm
#     https://drive.google.com/?tab=wo
#     https://www.google.com/intl/en/options/
#     http://www.google.com/history/optout?hl=en
#     . . . 
#

