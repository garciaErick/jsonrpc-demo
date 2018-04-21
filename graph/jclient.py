import socket
from bsonrpc import JSONRpc
from node import *
import json
from collections import namedtuple

leaf1 = Node("leaf1",0)
leaf2 = Node("leaf2",0)
graph = Node("root", 0,[leaf1, leaf1, leaf2])


# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))
rpc = JSONRpc(s)
server = rpc.get_peer_proxy()

Execute in server:
json_encoded_graph = server.increment(json_encode_graph(graph))

print(json_encode_graph(graph))
json_graph = json_encode_graph_by_reference(graph)
print(json_graph)
graph = json_decode_graph_with_references(json.loads(json_graph))
graph.show()
# print("Printing Graph")

print("")
print("From Client:")
print("Printing graph received from server")
graph = json_decode_graph(json.loads(json_encoded_graph))
graph.show()
rpc.close() # Closes the socket 's' also





