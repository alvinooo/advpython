#!/usr/bin/env python
# mylimit.py - Timer thread to limit process times
import sys
from threading import Timer
from subprocess import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

if (len(sys.argv) < 3):
    raise SystemExit("Usage: %s -sec command" %sys.argv[0])

time = float(sys.argv[1][1:]);  cmd = sys.argv[2:]

def terminate(process):
    debug("%s killed after %g seconds" %(cmd[0], time))
    process.kill()

procmd = Popen(cmd, stdout = PIPE) 
timer = Timer(time, terminate, [procmd])
timer.name = "Timer"

try:
    timer.start() 
    out = procmd.communicate()[0]
    if out: print out
except KeyboardInterrupt:
    sys.exit(1)
finally:
    timer.cancel()

###########################################################
#
#     $ mylimit.py -10 sleep 5
#
#     $ mylimit.py -5 sleep 10 
#     (Timer) sleep killed after 5 seconds
#
