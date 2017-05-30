# Track.py - Track class

class Track(object):
    def __init__(self, number=1, title="", length=""):
        self.__number = number         # track number
        self.__title = title           # track title 
        self.__length = length         # track length

    @property 
    def number(self): return self.__number
    @property 
    def title(self): return self.__title
    @property 
    def length(self): return self.__length

    def __str__(self):
        return "%d %s %s" \
            %(self.__number, self.__title, self.__length)
