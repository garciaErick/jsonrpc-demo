import socket
import node
from bsonrpc import JSONRpc
from json_services import *

def print_graph_addresses(root):
	print(root.name + " " + hex(id(root)))
	for child in graph.children:
		print("  " + child.name + " " + hex(id(child)))

leaf1 = Node("leaf1",0)
leaf2 = Node("leaf2",0)
graph = Node("root", 0,[leaf1, leaf1, leaf2])

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))
rpc = JSONRpc(s)
server = rpc.get_peer_proxy()

print("===========================================================================")
print("Pass to server without taking in account reference:")
print("===========================================================================")
print("From Client:")
print("Checking memory addresses:")
print_graph_addresses(graph)

# Execute in server:
json_encoded_graph = server.increment(json_encode_graph(graph))


print("")
print("From Client:")
print("Printing graph received from server")
graph = json_decode_graph(json.loads(json_encoded_graph))
graph.show()

print("")
print("Checking memory addresses:")
print_graph_addresses(graph)

print("")
print("===========================================================================")
print("Pass to server taking in account reference:")
print("===========================================================================")

leaf1 = Node("leaf1",0)
leaf2 = Node("leaf2",0)
graph = Node("root", 0,[leaf1, leaf1, leaf2])

		
print("From Client:")
print("Checking memory addresses:")
print_graph_addresses(graph)

# Execute in server:
json_encoded_graph = server.incrementByReference(json_encode_graph_by_reference(graph))


print("")
print("From Client:")
print("Printing graph received from server")
graph = json_decode_graph_with_references(json.loads(json_encoded_graph))
graph.show()
print("Checking memory addresses:")
print_graph_addresses(graph)

rpc.close() # Closes the socket 's' also





