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

