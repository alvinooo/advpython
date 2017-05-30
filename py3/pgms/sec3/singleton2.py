#!/usr/bin/env python3
# singleton2.py - Singleton metaclass, arg constrs, inhertiance

class Singleton(type): 
    def __init__(self, *args, **kwargs):
        print("Singleton constr")
        super().__init__(*args, **kwargs)
        self._instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            print("creating", self.__name__)
            self._instance = super().__call__(*args, **kwargs)
        return self._instance

class MySingleton(object, metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        print("MySingleton constr", args, kwargs)
    def write(self, data):
        print("write " + data)

class OtherSingleton(MySingleton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("OtherSingleton constr", args, kwargs)

one = MySingleton(3.4)
print("addr one: %x" %id(one))
two = MySingleton(12, "abc")
print("addr two: %x" %id(two))
one.write("data")
three = OtherSingleton("last")
print("addr three: %x" %id(three))

#################################################
#
#    $ singleton2.py
#    Singleton constr
#    Singleton constr
#    creating MySingleton
#    MySingleton constr (3.4,) {}
#    addr one: b6f3332c
#    addr two: b6f3332c
#    write data
#    creating OtherSingleton
#    MySingleton constr ('last',) {}
#    OtherSingleton constr ('last',) {}
#    addr three: b6f3340c
#
