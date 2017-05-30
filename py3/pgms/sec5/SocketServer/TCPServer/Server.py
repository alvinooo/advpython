# Server.py - TCP socketserver module
from socketserver import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class TCPHandler(StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        log(DEBUG, "received %s" %data)
        data = data.upper()
        self.wfile.write(data)
        log(DEBUG, "sent %s" %data)
        
class Server(TCPServer):
    def __init__(self, addr, handler = TCPHandler):
        TCPServer.__init__(self, addr, handler)
    def run(self):
        log(DEBUG, "waiting for requests")
        TCPServer.serve_forever(self)

