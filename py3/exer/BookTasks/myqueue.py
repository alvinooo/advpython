#!/usr/bin/env python3
# myqueue.py - Queue objects
from MyTask import MyTask
from TaskThread import *
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

mytask = MyTask("BookSQL")
task = TaskThread(mytask)

task.start()
task.send("""DELETE FROM BookCatalog WHERE 
title = 'Les Miserables'""")
task.send("""UPDATE BookCatalog SET copies = copies+1 
WHERE title = 'Jurassic Park'""")
task.close()

#################################################
#
#     $ myqueue.py
#     (MainThread) BookSQL file opened
#     (MainThread) put 'DELETE FROM BookCatalog WHERE
#     title = 'Les Miserables'' in queue
#     (MainThread) put 'UPDATE BookCatalog SET copies = copies+1 
#     WHERE title = 'Jurassic Park'' in queue
#     (MainThread) closing queue
#     (BookSQL) running sql: 'DELETE FROM BookCatalog WHERE 
#     title = 'Les Miserables''
#     (BookSQL) running sql: 'UPDATE BookCatalog SET copies = copies+1 
#     WHERE title = 'Jurassic Park''
#     (MainThread) closing task
#     (MainThread) BookSQL file closed
#
#     $ cat BookSQL
#     sql: DELETE FROM BookCatalog WHERE 
#     title = 'Les Miserables'
#     sql: UPDATE BookCatalog SET copies = copies+1 
#     WHERE title = 'Jurassic Park'
#
