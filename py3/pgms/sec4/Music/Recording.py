# Recording.py - Recording class

class Recording(object):
    def __init__(self, id=1, title="", artist="", category="",
                    label="", numTracks=0):
        self.__id = id                 # recording id 
        self.__title = title           # recording title 
        self.__artist = artist         # recording artist 
        self.__category = category     # recording category 
        self.__label = label           # recording label
        self.__numTracks = numTracks   # number of tracks

    @property 
    def id(self): return self.__id
    @property
    def title(self): return self.__title   
    @property
    def artist(self): return self.__artist
    @property
    def category(self): return self.__category
    @property
    def label(self): return self.__label
    @property
    def numTracks(self): return self.__numTracks

    def __str__(self):
        return "%d %s %s %s %s %d" \
            %(self.__id, self.__title, self.__artist,
                self.__category, self.__label, self.__numTracks)

