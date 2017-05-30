# Server.py - UDP SocketServer module
from SocketServer import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class UDPHandler(DatagramRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        log(DEBUG, "received %s" %data)
        data = data.upper()
        self.wfile.write(data)
        log(DEBUG, "sent %s" %data)
        
class Server(UDPServer):
    def __init__(self, addr, handler = UDPHandler):
        UDPServer.__init__(self, addr, handler)
    def run(self):
        log(DEBUG, "waiting for requests")
        UDPServer.serve_forever(self)

