# Server.py - custom TCP SocketServer module
from SocketServer import TCPServer
from Handler import MyRequestHandler
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class Server(TCPServer):
    def __init__(self, addr, handler = MyRequestHandler):
        log(DEBUG, "__init__")
        TCPServer.__init__(self, addr, handler)

    def server_activate(self):
        log(DEBUG, "server_activate")
        TCPServer.server_activate(self)

    def run(self):
        log(DEBUG, "waiting for requests")
        TCPServer.serve_forever(self)

    def verify_request(self, request, client):
        log(DEBUG, "verfy_request %s %s" %client)
        return TCPServer.verify_request(self, request, client)

    def process_request(self, request, client):
        log(DEBUG, "process_request %s %s" %client)
        return TCPServer.process_request(self, request, client)

    def finish_request(self, request, client):
        log(DEBUG, "finish_request %s %s" %client)
        return TCPServer.finish_request(self, request, client)
        
    def close_request(self, request):
        log(DEBUG, "close_request")
        return TCPServer.close_request(self, request)

