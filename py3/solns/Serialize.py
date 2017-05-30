# Serialize.py - Serialize module
import pickle

def save(filename, obj, priority=1):
    file = open(filename, "wb")
    pickle.dump(obj, file, priority)
    file.close()

def restore(filename):
    file = open(filename, "rb")
    obj = pickle.load(file)
    file.close()
    return obj
