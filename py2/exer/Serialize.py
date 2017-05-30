# Serialize.py - Serialize module
import pickle

# your save() function here...
def save(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

# your restore() function here...
def restore(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
