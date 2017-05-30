#!/usr/bin/env python3
# events.py - Event objects
from Media import Media
from threading import *
from time import sleep 
from logging import *
basicConfig(level=DEBUG, format="(%(threadName)s) %(message)s",)

def loadVideo(media):
    debug("loading %s video..." %media._title)
    sleep(2)
    media.playVideo()

def loadAudio(media):
    debug("loading %s audio..." %media._title)
    sleep(1)
    media.playAudio()

mp4 = Media("mp4")
Thread(target=loadVideo, name="Video", 
    args=(mp4,)).start()
Thread(target=loadAudio, name="Audio", 
    args=(mp4,)).start()

mainThread = current_thread()
for thread in enumerate():
    if thread is not mainThread:
        thread.join()
debug("%s done" %mp4._title)

#################################################
#
#     $ events.py
#     (Video) loading mp4 video...
#     (Audio) loading mp4 audio...
#     (Video) playing mp4 video at 380761
#     (Audio) playing mp4 audio at 380977
#     (MainThread) mp4 done
#
