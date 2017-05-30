#!/usr/bin/env python
# mymodule.py - commas function

def commas(arg):
    print "Python: commas('%s') invoked" %arg
    if (type(arg) is str):
        return "{:,}".format(int(arg))
    raise TypeError("%s is not a string" %arg)

if __name__ == "__main__":     # run as main program
    import sys
    if (len(sys.argv) < 2):
        raise SystemExit("Usage: %s number" %sys.argv[0])

    number = sys.argv[1]
    print commas(number)

##########################################
#
#    $ mymodule.py 123
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
