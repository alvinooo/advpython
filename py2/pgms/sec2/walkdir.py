#!/usr/bin/env python
# walkdir.py - walk directory tree
import sys, os
from stat import *

topdir = "." if len(sys.argv) == 1 else sys.argv[1]
if not os.path.isdir(topdir):
    raise SystemExit("Usage: %s dir" %sys.argv[0])

def getstat(name, dirname):
    rootbase = os.path.split(os.path.abspath(name))
    path = os.path.join(rootbase[0], dirname, name)
    info = (mode, inode, dev, nlinks, uid, gid, size,
        atime, ctime, mtime) = os.stat(path)
    return info

for (dirname, dirlist, filelist) in os.walk(topdir):
    print "%s:" %dirname
    for file in filelist:
        info = getstat(file, dirname)
        print "\tfile %s: len = %d perm mode = %s" \
            %(file, info[ST_SIZE], 
                str(oct(info[ST_MODE]))[4:])
    for dir in dirlist:
        info = getstat(dir, dirname)
        print "\tdir %s: perm mode = %s" \
            %(dir, str(oct(info[0]))[3:])

###############################################
#
#    $ walkdir.py mydir
#    mydir:
#        file base: len = 26220 perm mode = 444
#        file alpha: len = 54916 perm mode = 644
#        dir subdir1: perm mode = 700
#    mydir/subdir1:
#        file random: len = 1700 perm mode = 775
#        file number: len = 56 perm mode = 644
#
