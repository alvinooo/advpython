# tracing.py - tracing module
from functools import wraps

trace = { "enable" : True }
mylog = open("logfile", "w")

def tracing(func):
    if (trace["enable"]):
        @wraps(func)
        def invoke(*args, **kwargs):
            mylog.write("Invoking %s: %s %s\n"
                %(func.__name__, args, kwargs))
            retval = func(*args, **kwargs) 
            mylog.write("%s returned from: %s\n"
                %(func.__name__, retval))
            return retval
        return invoke
    else:
        return func
