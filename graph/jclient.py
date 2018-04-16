import socket
from bsonrpc import JSONRpc
from node import *
import json
from collections import namedtuple

leaf1 = node("leaf1")
leaf2 = node("leaf2")
graph = node("root", [leaf1, leaf1, leaf2])

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))
rpc = JSONRpc(s)
server = rpc.get_peer_proxy()

# Execute in server:
json_encoded_graph = server.increment(json_encode_graph(graph))
rpc.close() # Closes the socket 's' also





