# Server.py - forking TCP socketserver module
from os import *
from subprocess import *
from socketserver import *
from logging import *
basicConfig(level=DEBUG, format="Server: %(message)s",)

class ForkingHandler(StreamRequestHandler):
    def handle(self):
        pid = getpid()                         # process id
        dup2(open("/dev/null", O_RDONLY), 0)   # redirect stdin
        cmd = self.rfile.readline().strip().decode("ascii")
        log(DEBUG, "received '%s'" %cmd)
        try:
            output = check_output(cmd, shell=True).splitlines()
            response = "\n".encode("ascii").join(output)
            self.wfile.write(response)
            log(DEBUG, "process %s sent %s" %(pid, response))
        except CalledProcessError:
            msg = "error with '%s'" %cmd
            self.wfile.write(msg.encode("ascii"))
        
class Server(ForkingMixIn, TCPServer):
    def __init__(self, addr, handler = ForkingHandler):
        super(Server, self).__init__(addr, handler)
    def run(self):
        log(DEBUG, "waiting for commands")
        TCPServer.serve_forever(self)


