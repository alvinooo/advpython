# Factory.py - create object dynamically

def createObject(classfile = "classnames"):
    with open(classfile) as file:
        line = file.read()[:-1]
    args = line.split()
    (modulename, classname) = args[0].split(".")
    module = __import__(modulename, globals(), locals(),[classname])
    return getattr(module, classname)(*args[1:])   # call __init__
