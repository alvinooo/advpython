#!/usr/bin/env python3
# mytasks.py - consumer tasks
from multiprocessing import *
from Consumer import Consumer
from Task import Task

if __name__ == "__main__":
    tasks = JoinableQueue()
    results = Queue()
    numCores = cpu_count() 
    print("Number of cores = %d" %numCores)

    consumers = [Consumer(tasks, results) for n in range(numCores*2)]
    for consumer in consumers:
        consumer.start()                 # start consumer

    urls = ["ibm.com", "apple.com"]; NLINKS = 3 
    for url in urls:
        tasks.put(Task(url, NLINKS))     # find first NLINKS in url
    for consumer in consumers:
        tasks.put(None)                  # terminate consumer
    tasks.join()                         # wait for all tasks to finish

    for url in urls:
        print(results.get())             # show links

##################################################
#
#     $ mytasks.py
#     Number of cores = 1
#     (Consumer-2) process 10763: ibm.com
#     (Consumer-2) found 3 links for ibm.com
#     (Consumer-1) process 10762: apple.com
#     (Consumer-1) found 3 links for apple.com
#     (Consumer-1) Exiting
#     (Consumer-2) Exiting
#     ['http://www.w3.org/1999/xhtml', 'http://www.apple.com/', 
#     'http://www.apple.com/']
#     ['http://www.ibm.com/us-en/', 'http://schema.org', 
#     'http://www.ibm.com']
#
