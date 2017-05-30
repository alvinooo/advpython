# Music.py - Music class, singleton
import sqlite3
from Singleton import Singleton
from Recording import Recording
from Track import Track

class Music(object, metaclass=Singleton):
    def __init__(self, database):
        self.__database = database
        self.__conn = sqlite3.connect(database)
        self.__conn.row_factory = sqlite3.Row
    def __del__(self):
        self.__conn.close()

    @property
    def database(self):   
        return self.__database

    def getMusicCategories(self):
        cursor = self.__conn.execute("""
            SELECT * FROM 'Music Categories'
        """) 
        categories = cursor.fetchall()
        return [name["MusicCategory"] for name in categories]

    def getRecordings(self):
        cursor = self.__conn.execute("""
           SELECT Recordings.*, 
              'Recording Artists'.RecordingArtistName,
                 'Music Categories'.MusicCategory FROM Recordings,
                    'Recording Artists', 'Music Categories' WHERE
                       Recordings.RecordingArtistID = 
                          'Recording Artists'.RecordingArtistID AND
                             Recordings.MusicCategoryID =
                                'Music Categories'.MusicCategoryID
        """) 
        return [ Recording(
                   row["RecordingID"], 
                   row["RecordingTitle"],
                   row["RecordingArtistName"], 
                   row["MusicCategory"],
                   row["RecordingLabel"], 
                   row["NumberofTracks"])
               for row in cursor ]

    def getTracks(self, recording):
        cursor = self.__conn.execute("""
           SELECT * FROM Tracks WHERE RecordingID = ?
               ORDER by TrackNumber""",
                 (recording.id,))
        return [ Track(
                   row["TrackNumber"], 
                   row["TrackTitle"],
                   row["TrackLength"]) 
               for row in cursor ]

