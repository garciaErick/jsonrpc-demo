import json
import uuid

class Node:
    def __init__(self, name, val, children = []):
        self.name = name
        self.children = children
        self.val = val

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
        children.append(Node(child["name"], child["val"]))
    return Node(json_graph["name"], json_graph["val"], children)

def json_decode_graph_with_references(json_graph):
    graph = add_nodes_and_references(json_graph)
    graph = add_missing_instances_by_reference(graph, graph)
    graph = remove_keys(graph)
    return graph

def add_nodes_and_references(json_graph):
    children = dict()
    for id, child in json_graph["children"].items():
        if "children" not in child:
            children[str(id)] = str(child)
        else:
            add_nodes_and_references(child)
            children[str(id)] = Node(child["name"], child["val"])
    return Node(json_graph["name"], json_graph["val"], children)

def add_missing_instances_by_reference(graph_with_references, root):
    #todo: transverse the whole graph
    if isinstance(graph_with_references.children, dict): 
        for id, child in graph_with_references.children.items():
            if isinstance(child, Node): 
                add_missing_instances_by_reference(child, root)
            if not isinstance(child, Node):
                node_reference = find_node_by_id(root, child)
                graph_with_references.children[id] = node_reference
    return root

def find_node_by_id(root, ref_id):
    if isinstance(root, Node):
        if isinstance(root.children, dict): 
            for child in root.children.values():
                find_node_by_id(child, ref_id)
            if ref_id in root.children.keys():
                return root.children[ref_id]
    else:
        return #not found

def remove_keys(graph_with_ids):
    if isinstance(graph_with_ids.children, dict): 
        children = []
        for child in graph_with_ids.children.values():
            remove_keys(child)
            children.append(child)
        graph_with_ids.children = children
        return graph_with_ids

def json_encode_graph(graph):
    children = []
    for child in graph.children:
        children.append(child.__dict__)
        json_encode_graph(child)
    setattr(graph, 'children', children)
    json_graph = json.dumps(graph.__dict__)
    return json_graph

def json_encode_graph_by_reference(graph):
    children = dict()
    for child in graph.children:
        if id(child) in children:
            guid = uuid.uuid4().hex[:15].upper()
            id_of_duplicate_child = str(id(child))
            children[guid] = id_of_duplicate_child
        children[id(child)] = child.__dict__
        json_encode_graph_by_reference(child)
    setattr(graph, 'children', children)
    json_graph = json.dumps(graph.__dict__)
    return json_graph
