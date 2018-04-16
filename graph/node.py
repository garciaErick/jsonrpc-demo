import json

class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0

    def show(self, level=0):
        print "%s%s val=%d:" % (level*"  ", self.name, self.val)
        for c in self.children: 
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def json_decode_graph(json_graph):
    children = []
    for child in json_graph["children"]:
        json_decode_graph(child)
        children.append(node(child["name"]))
    return node(json_graph["name"], children)

def json_encode_graph(graph):
    children = []
    for child in graph.children:
        children.append(child.__dict__)
        json_encode_graph(child)
    setattr(graph, 'children', children)
    json_graph = json.dumps(graph.__dict__)
    return json_graph
