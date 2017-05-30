# MyType.py - Typing with metaclass

class PropertyType(object):
    def __init__(self, type, value = None):
        print "PropertyType: __init__", type
        self.name = None
        self.type = type
        self.value = type() if value is None else value

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.value)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("attribute must be a %s" %self.type)
        setattr(instance, self.name, value)
    def __delete__(self, instance):
        raise AttributeError("can't delete attribute")

class TypeMeta(type):
    def __new__(cls, name, bases, attrs):
        print "TypeMeta: __new__", name
        newclass = super(TypeMeta, cls).__new__(cls, name, bases, attrs)
        slots = []
        for (key, value) in attrs.items():
            #print key, value
            if isinstance(value, PropertyType):
                value.name = "_" + key
                slots.append(value.name)
        setattr(cls, "__slots__", slots)
        return newclass

class MyType(object):
    __metaclass__ = TypeMeta
