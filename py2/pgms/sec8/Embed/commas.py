#!/usr/bin/env python
# commas.py - encode commas for numbers
import sys

if (len(sys.argv) < 2):
    raise SystemExit("Usage: %s number" %sys.argv[0])

input = int(sys.argv[1])
print "{:,}".format(input)

##########################################

#    $ commas.py 123
#    123
#    $ commas.py 1234
#    1,234
#    $ commas.py 12345
#    12,345
#    $ commas.py 123456
#    123,456
#    $ commas.py 1234567
#    1,234,567
#    $ commas.py 12345678
#    12,345,678
#    $ commas.py 123456789
#    123,456,789
#
