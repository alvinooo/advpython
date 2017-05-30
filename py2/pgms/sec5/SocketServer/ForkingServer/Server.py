# Server.py - forking TCP SocketServer module
from os import *
from subprocess import *
from SocketServer import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class ForkingHandler(StreamRequestHandler):
    def handle(self):
        pid = getpid()                         # process id
        dup2(open("/dev/null", O_RDONLY), 0)   # redirect stdin
        cmd = self.rfile.readline().strip()    # get command
        log(DEBUG, "received '%s'" %cmd)
        try:
            output = check_output(cmd, shell=True).splitlines()
            response = "\n".join(output)
            self.wfile.write(response)
            log(DEBUG, "process %s sent %s" %(pid, response))
        except CalledProcessError:
            self.wfile.write("error with '%s'" %cmd)
        
class Server(ForkingMixIn, TCPServer):
    def __init__(self, addr, handler = ForkingHandler):
        TCPServer.__init__(self, addr, handler)
    def run(self):
        log(DEBUG, "waiting for commands")
        TCPServer.serve_forever(self)

