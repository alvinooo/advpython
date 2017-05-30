#!/usr/bin/env python3
# flocked.py - file locking
import sys
from os import *
from fcntl import *
from time import sleep
from struct import pack

NAP = 3          # sleep time
fd = open("testfile", O_RDWR)

mystruct = pack("hhllhh", F_WRLCK, 0, 0, 0, 0, 0)
fcntl(fd, F_SETLKW, mystruct)   # lock file
print("process %d locked file" %getpid())
sleep(NAP)

mystruct = pack("hhllhh", F_UNLCK, 0, 0, 0, 0, 0)
print("process %d unlocking file" %getpid())
fcntl(fd, F_SETLKW, mystruct)   # unlock file
close(fd)                       # close file

###############################################
#
#    $ flocked.py &
#    [1] 6066 
#    process 6066 locked file
#    process 6066 unlocked file
#    [1]+ Done  flocked.py
#
#    $ flocked.py & flocked.py &
#    [1] 6068 
#    [1] 6069 
#    process 6068 locked file
#    process 6068 unlocked file
#    process 6069 locked file
#    process 6069 unlocked file
#    [1]- Done  flocked.py
#    [2]+ Done  flocked.py
# 
