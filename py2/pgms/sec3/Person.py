# Person.py - Person class

class Person(object):
    _noName = ""                     # default name
    _noAge = 18                      # default age
    def __init__(self, name=_noName, age=_noAge):
        self.name = name             # getter and setter
        self.age = age               # calls setter

    @property                        # age property getter
    def age(self): 
        return self.__age

    @age.setter                      # age property setter
    def age(self, age):  
        if (age <= 0):
            raise ValueError("Person has bad age %d" %age)
        self.__age = age

    def __str__(self):               # string method
        return "Name: %s Age: %d" %(self.name, self.age)

