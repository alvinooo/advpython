# BoundList.py - Bounded list

class BoundList:
    def __init__(self, lb, ub): 
        if (lb > ub):
            raise ValueError(
                "BoundList has bad bounds (%d, %d)" %(lb, ub))
        self.__lower = lb
        self.__upper = ub
        self.__list = [0]*(ub-lb+1)

    @property
    def lower(self):
        return self.__lower

    @property
    def upper(self):
        return self.__upper

    def length(self):
        return self.upper-self.lower+1

    def __range(self, index):
        if (index < self.lower or index > self.upper):
            raise IndexError("BoundList has bad index %d" %index)

    def __getitem__(self, index):          # indexing
        self.__range(index)
        return self.__list[index-self.lower]

    def __setitem__(self, index, value):   # index assign
        self.__range(index)
        self.__list[index-self.lower] = value

    def getRange(self):
       return list(range(self.lower, self.upper+1))

