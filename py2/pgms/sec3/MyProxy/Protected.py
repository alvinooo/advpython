# Protected.py - Protected proxy

def public(func):
    func.__public__ = True
    return func

class Protected(object):
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)

        def __getattr__(self, name):
            attr = getattr(obj, name)
            if hasattr(attr, "__public__"):
                return attr
            elif hasattr(cls, "__public__"):
                if name in cls.__public__:
                    return attr
            raise AttributeError, "%s is not public" %name

        def __setattr__(self, name, value):
            attr = getattr(obj, name)
            cls.__setattr__(self, name, value)

        Proxy = type("Protected(%s)" %cls.__name__, (), {})

        for name in dir(cls):
            if name not in dir(Proxy) and \
                    name.startswith("__") and name.endswith("__"):
                try:
                    setattr(Proxy, name, getattr(obj, name))
                except TypeError: 
                    pass

        Proxy.__getattr__ = __getattr__
        Proxy.__setattr__ = __setattr__
        return Proxy()

