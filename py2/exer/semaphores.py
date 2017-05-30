#!/usr/bin/env python
# semaphores.py - semaphores with data
from MyData import MyData
from threading import *
from time import sleep
from random import random
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def writer(myData, data):
    pause = random()
    sleep(pause)
    myData.writeData(data)

def reader(myData):
    pause = random()
    sleep(pause)
    debug("%s" %myData.readData())
            
mydata = ["data1", "data2"]

data = MyData("start")
for num in range(2):
    Thread(target=writer, name="Writer", 
        args=(data, mydata[num])).start()
    Thread(target=reader, name="Reader",
        args=(data,)).start()

mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        thread.join()

#################################################
#
#     $ semaphores.py
#     (Reader) data1
#     (Reader) data2
#
#     $ semaphores.py
#     (Reader) data2
#     (Reader) data1
#     
