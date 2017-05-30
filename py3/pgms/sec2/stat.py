#!/usr/bin/env python3
# stat.py - file status IDs
import os, pwd, grp, time

(mode, inode, dev, nlinks, uid, gid, size,
    atime, ctime, mtime) = os.stat("stat.py")

print("file mode", oct(mode))
print("inode", inode)
print("major device", os.major(dev))
print("minor device", os.minor(dev))
print("number of links", nlinks)
print("user name:", pwd.getpwuid(uid)[0])
print("group name:", grp.getgrgid(gid)[0])
print("file length", size)
print("time of last access", time.ctime(atime))
print("time of last modification", time.ctime(mtime))
print("time of last stat change", time.ctime(ctime))

###############################################
#
#    $ stat.py
#    file mode 0100755
#    inode 424509
#    major device 8
#    minor device 1
#    number of links 1
#    user name: paul
#    group name: paul
#    file length 648
#    time of last access Sat Oct 15 17:04:57 2016
#    time of last modification Sat Oct 15 17:04:56 2016
#    time of last stat change Sat Oct 15 17:04:56 2016
# 
