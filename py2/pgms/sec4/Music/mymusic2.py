#!/usr/bin/env python
# mymusic2.py - Music database, get tracks
from Music import Music

music = Music("Music.db")
recordings = music.getRecordings()
recording = recordings[5]   # get a recording

print "Tracks for Recording", recording.title
tracks = music.getTracks(recording)
for track in tracks:
    print track

#################################################
#
#  $ mymusic2.py
#  Tracks for Recording Stay Awhile
#  1 Gypsy Girl 4:14
#  2 You Stole Their Hearts 3:47
#  3 Stay Awhile 3:41
#  4 When You're Close 3:53
#  5 I Wouldn't Mind Knowing 3:12
#  6 Birds Hover 4:32
#  7 Sweet Little Angel of Mine 2:48
#  8 Psychic Hotline 4:16
#  9 Showtime Baby 3:53
#  10 Fell In and Fallen 4:13
#  11 Fourteen Years 3:47
#  12 Louise 3:06
#  13 Whoever Brought You Near 2:17
# 
