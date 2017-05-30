#!/usr/bin/env python
# people.py - Student, Person program
from Person import Person
from Student import Student

try:
    person1 = Person("Bob", 28)
    person2 = Person("Jack", 42)
    person3 = Student("Mary", 38, "English", 3.5)
    person4 = Student("Joe", 31)
    person4.major = "Math"
    person4.gpa = 3.8

    for person in (person1, person2, person3, person4):
        print person

    # people over 35
    # your code here...
    print [person.name for person in [person1, person2, person3, person4] if person.age > 35]
except Exception as ex:
    raise SystemExit("%s" %ex)

#################################################
#
#    $ people.py
#    Name: Bob Age: 28
#    Name: Jack Age: 42
#    Name: Mary Age: 38 Major: English GPA: 3.5
#    Name: Joe Age: 31 Major: Math GPA: 3.8
#    ['Jack', 'Mary']
#
