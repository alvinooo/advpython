# Student.py - Student class
from Person import Person

class Student(Person):
    _noMajor = "undeclared"            # default major
    _noGpa = 0.0                       # default gpa
    def __init__(self, name=Person._noName, age=Person._noAge, 
            major=_noMajor, gpa=_noGpa):
        super(Student, self).__init__(name, age)
        self.major = major             # getter and setter
        self.gpa = gpa                 # calls setter

    @property                          # gpa property getter
    def gpa(self):
        return self.__gpa

    @gpa.setter                        # gpa property setter
    def gpa(self, gpa):
        if (gpa < 0.0):
            raise ValueError("Student has bad gpa %g" %gpa)
        self.__gpa = gpa

    def __str__(self):                 # string method
        return "%s Major: %s GPA: %g" %(Person.__str__(self), 
             self.major, self.gpa)

