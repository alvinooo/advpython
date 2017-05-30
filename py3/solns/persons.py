#!/usr/bin/env python3
# persons.py - Person program
from Person import Person

try:
    person1 = Person("Bob", 28)
    person2 = Person("Jack", 42)
    person3 = Person("Mary", 38)
    person4 = Person()
    person4.name = "Jim"
    person4.age = 35

    for person in (person1, person2, person3, person4):
        print(person)

    oldest = max([p.age for p in (person1, person2, person3, person4)])
    print("oldest age is %d" %oldest)
except Exception as ex:
    raise SystemExit("%s" %ex)

#################################################
#
#    $ persons.py
#    There are 4 people
#    Name: Bob Age: 28
#    Name: Jack Age: 42
#    Name: Mary Age: 38
#    Name: Jim Age: 35
#    oldest age is 42
#
