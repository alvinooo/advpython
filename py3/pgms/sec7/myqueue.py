#!/usr/bin/env python3
# myqueue.py - Queue objects
from MyTask import MyTask
from TaskThread import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

mytask = MyTask("URLlinks")
task = TaskThread(mytask)

task.start()
task.send("google.com")
task.send("ibm.com")
#task.send("apple.com")
#task.send("cnn.com")
#task.send("espn.com")
debug("do something else")
task.close()

#################################################
#
#     $ myqueue.py
#     (MainThread) file opened
#     (MainThread) put 'google.com' in queue
#     (MainThread) put 'ibm.com' in queue
#     (MainThread) do something else
#     (MainThread) closing queue
#     (URLlinks) finding links for google.com
#     (URLlinks) finding links for ibm.com
#     (MainThread) closing task
#     (MainThread) file closed
#
