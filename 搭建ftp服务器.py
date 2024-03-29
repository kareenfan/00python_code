

# FTP server

import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
fh = logging.FileHandler(filename="myftpserver.log", encoding='utf-8')
ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())
logger.addHandler(ch)
logger.addHandler(fh)

authorizer = DummyAuthorizer()
authorizer.add_user("fanjj", "123123", "d:/", perm="elradfmwM")
authorizer.add_anonymous(homedir="d:/")

handler = FTPHandler
handler.authorizer = authorizer
handler.passive_ports = range(2000, 2333)

dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 30000 * 1024
dtp_handler.write_limit = 30000 * 1024
handler.dtp_handler = dtp_handler

server = FTPServer(("0.0.0.0", 2121), handler)
server.max_cons = 150
server.max_cons_per_ip = 15
server.serve_forever()
