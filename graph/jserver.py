# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
import node
import json
from node import *
from bsonrpc import JSONRpc
from bsonrpc import request, service_class

# Class providing functions for the client to use:
@service_class
class ServerServices(object):

	@request
	def increment(self, json_encoded_graph):
		print("From Server:")
		print("Graph before increment:")
		graph = json_decode_graph(json.loads(json_encoded_graph))
		graph.show()

		increment(graph)
		print("")
		print("Graph after increment:")
		graph.show()
		return json_encode_graph(graph)

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
	s, _ = ss.accept()
	# JSONRpc object spawns internal thread to serve the connection.
	JSONRpc(s, ServerServices())
Client
import socket
from bsonrpc import JSONRpc
