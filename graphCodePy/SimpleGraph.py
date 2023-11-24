class Vertex:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self.incident_edge_list = []

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, v1, v2, data, name):
        self.v1 = v1
        self.v2 = v2
        self.data = data
        self.name = name

    def __str__(self):
        return self.name

    def get_first_endpoint(self):
        return self.v1

    def get_second_endpoint(self):
        return self.v2

class SimpleGraph:
    def __init__(self):
        self.vertex_list = []
        self.edge_list = []

    def vertices(self):
        return iter(self.vertex_list)

    def edges(self):
        return iter(self.edge_list)

    def incident_edges(self, v):
        return iter(v.incident_edge_list)

    def a_vertex(self):
        if self.vertex_list:
            return self.vertex_list[0]
        else:
            return None

    def insert_vertex(self, data, name):
        v = Vertex(data, name)
        self.vertex_list.append(v)
        return v

    def insert_edge(self, v1, v2, data, name):
        e = Edge(v1, v2, data, name)
        self.edge_list.append(e)
        v1.incident_edge_list.append(e)
        v2.incident_edge_list.append(e)
        return e

    def opposite(self, v, e):
        if e.get_first_endpoint() == v:
            return e.get_second_endpoint()
        elif e.get_second_endpoint() == v:
            return e.get_first_endpoint()
        else:
            return None

    def num_vertices(self):
        return len(self.vertex_list)

    def num_edges(self):
        return len(self.edge_list)

# Example usage
G = SimpleGraph()
a = G.insert_vertex(None, "a")
b = G.insert_vertex(None, "b")
c = G.insert_vertex(None, "c")
x = G.insert_edge(a, b, None, "X")
y = G.insert_edge(b, c, None, "Y")

print("Iterating through vertices...")
for v in G.vertices():
    print(f"found vertex {v}")

print("Iterating through adjacency lists...")
for v in G.vertices():
    print(f"Vertex {v}")
    for e in G.incident_edges(v):
        print(f"  found edge {e}")

print("Testing opposite...")
print(f"opposite(a, x) is {G.opposite(a, x)}")
print(f"opposite(a, y) is {G.opposite(a, y)}")
print(f"opposite(b, x) is {G.opposite(b, x)}")
print(f"opposite(b, y) is {G.opposite(b, y)}")
print(f"opposite(c, x) is {G.opposite(c, x)}")
print(f"opposite(c, y) is {G.opposite(c, y)}")
