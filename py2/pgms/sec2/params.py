#!/usr/bin/env python
# params.py - process parameters
import os

print "My process id is %d" %os.getpid()
print "My parent's process is %d\n" %os.getppid()

print "User is %s" %os.environ["USER"]
print "User, group id's are %d, %d\n" \
    %(os.getuid(), os.getgid())

(sys, node, release, vers, machine) = os.uname()
print "System name is", sys
print "Node name is", node
print "System release is", release
print "System version is", vers
print "System machine is", machine
    
###############################################
#
#    $ params.py
#    My process id is 7289
#    My parent's process is 7288
#
#    User is paul
#    User, group id's are 1000, 1000
#
#    System name is Linux
#    Node name is paul-VirtualBox
#    System release is 3.2.0-35-generic-pae
#    System version is #55-Ubuntu SMP Wed Dec 5 18:04:39 UTC 2012
#    System machine is i686
# 
