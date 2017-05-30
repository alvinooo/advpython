# Handler.py - Handler module
from socketserver import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class MyRequestHandler(StreamRequestHandler):
    def setup(self):
        log(DEBUG, "handler setup")
        return StreamRequestHandler.setup(self)
        
    def handle(self):
        data = self.rfile.readline().strip()
        log(DEBUG, "handler received %s" %data)
        data = data.upper()
        self.wfile.write(data)
        log(DEBUG, "handler sent %s" %data)
        
    def finish(self):
        log(DEBUG, "handler finish")
        return StreamRequestHandler.finish(self)
        

