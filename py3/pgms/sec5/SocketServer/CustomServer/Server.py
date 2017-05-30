# Server.py - custom TCP socketserver module
from socketserver import TCPServer
from Handler import MyRequestHandler
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class Server(TCPServer):
    def __init__(self, addr, handler = MyRequestHandler):
        log(DEBUG, "__init__")
        super(Server, self).__init__(addr, handler)

    def server_activate(self):
        log(DEBUG, "server_activate")
        super(Server, self).server_activate()

    def run(self):
        log(DEBUG, "waiting for requests")
        super(Server, self).serve_forever()

    def verify_request(self, request, client):
        log(DEBUG, "verfy_request %s %s" %client)
        return super(Server, self).verify_request(request, client)

    def process_request(self, request, client):
        log(DEBUG, "process_request %s %s" %client)
        return super(Server, self).process_request(request, client)

    def finish_request(self, request, client):
        log(DEBUG, "finish_request %s %s" %client)
        return super(Server, self).finish_request(request, client)

    def close_request(self, request):
        log(DEBUG, "close_request")
        return super(Server, self).close_request(request)

