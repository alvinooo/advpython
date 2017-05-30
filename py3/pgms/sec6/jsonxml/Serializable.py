# Serializable.py - Serializable module
import json
from collections import OrderedDict

registry = {}
def register(cls):
    registry[cls.__name__] = cls

def deserialize(data):
    params = json.loads(data)
    name = params["class"]
    cls = registry[name]
    return cls(*params["args"])

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        newclass = super(MetaClass, cls).__new__(cls, name, bases, attrs)
        register(newclass)
        return newclass 

class Serializable(object, metaclass=MetaClass):
    def __init__(self, *args):
        self.__args = args
    def serialize(self):
        data = OrderedDict()
        data["class"] = self.__class__.__name__
        data["args"] = self.__args
        return json.dumps(data)

