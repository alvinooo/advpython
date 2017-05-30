# Student.py - Student class
from Person import Person

class Student(Person):
    # your code here...
    _major = ""
    _gpa = 0
    def __init__(self, name, age, major=_major, gpa=_gpa):
        super(Student, self).__init__(name, age)
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return "%s Major: %s GPA: %.1f" % (Person.__str__(self), self.major, self.gpa)

