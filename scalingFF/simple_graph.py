from vertex import Vertex
from edge import Edge

class SimpleGraph:
    def __init__(self):
        self.vertex_list = []
        self.edge_list = []
        self.source = None
        self.sink = None
        self.max_capacity = 0

    def incident_edges(self, v: Vertex):
        return v.incident_edge_list
    
    def get_edge(self, v1: Vertex, v2:Vertex):
        for e in v1.out_edge_list:
            if e.v2 == v2:
                return e
        return None

    def insert_vertex(self, name: str):
        v = Vertex(name)
        self.vertex_list.append(v)
        if name == 's':
            self.source = v
        if name == 't':
            self.sink = v
        return v

    def insert_edge(self, v1, v2, data: int):
        e = Edge(v1, v2, data)
        self.edge_list.append(e)
        v1.out_edge_list.append(e)
        v2.in_edge_list.append(e)
        self.max_capacity = max(self.max_capacity, data)
        return e

    def opposite(self, v: Vertex, e: Edge):
        if e.v1 == v:
            return e.v2
        elif e.v2 == v:
            return e.v1
        else:
            return None

    def num_vertices(self):
        return len(self.vertex_list)

    def num_edges(self):
        return len(self.edge_list)

    
# G = SimpleGraph()
# a = G.insert_vertex("a")
# b = G.insert_vertex("b")
# c = G.insert_vertex("c")
# x = G.insert_edge(a, b, 12)
# y = G.insert_edge(b, c, 9)

# print("Iterating through vertices...")
# for v in G.vertex_list:
#     print(f"found vertex {v}")

# print("Iterating through adjacency lists...")
# for v in G.vertex_list:
#     print(f"Vertex {v}")
#     for e in G.incident_edges(v):
#         print(f"  found edge {e}")

# print("Testing opposite...")
# print(f"opposite(a, x) is {G.opposite(a, x)}")
# print(f"opposite(a, y) is {G.opposite(a, y)}")
# print(f"opposite(b, x) is {G.opposite(b, x)}")
# print(f"opposite(b, y) is {G.opposite(b, y)}")
# print(f"opposite(c, x) is {G.opposite(c, x)}")
# print(f"opposite(c, y) is {G.opposite(c, y)}")
