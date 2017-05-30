# Book.py - Book class

class Book(object):
    def __init__(self, id=1, author="", title="", notes="", copies=1):
        self.__id = id                 # book id 
        self.__author = author         # book author 
        self.__title = title           # book title 
        self.__notes = notes           # book notes 
        self.__copies = copies         # number of copies

    @property
    def id(self): return self.__id
    @property
    def author(self): return self.__author
    @property
    def title(self): return self.__title
    @property
    def notes(self): return self.__notes
    @property
    def copies(self): return self.__copies

    def __str__(self):
        return "%d %s %s %s %d" \
            %(self.__id, self.__author, self.__title, 
                self.__notes, self.__copies)

