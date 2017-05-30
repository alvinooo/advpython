#!/usr/bin/env python3
# mymusic.py - access Music database
from Music import Music

music = Music("Music.db")
print("Music Categories in %s" %music.database)
categories = music.getMusicCategories()
for name in categories:
    print("%s," %name, end=' ')
print("\n")

print("Music Recordings in %s" %music.database)
recordings = music.getRecordings()
for recording in recordings:
    print(recording)

#################################################
#
#  $ mymusic.py
#  Music Categories in Music.db
#  Classical, Rock, Jazz, Rap, Country, Musical Theatre, Blues,
#
#  Music Recordings in Music.db
#  1 Orff: Carmina Burana The Philadelphia Orchestra Classical Sony Classical 11
#  2 Doors Doors Rock Elektra 11
#  3 Imagine John Lennon Rock Warner Brothers 21
#  4 Santana Santana Rock Columbia 9
#  5 Graceland Paul Simon Rock Warner Brothers 11
#  6 Stay Awhile Isam Band Rock Spragueland 13
#  7 Sgt. Pepper's Lonely Hearts Club Band Beatles Rock EMI Records 12
#
