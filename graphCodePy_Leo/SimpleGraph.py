# SimpleGraph.py
from edge import Vertex, Edge

class SimpleGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def insert_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
        return self.vertices[name]

    def insert_edge(self, v1: Vertex, v2: Vertex, capacity, name=None):
        edge = Edge(v1, v2, capacity, name)
        self.edges.append(edge)

    def find_edge(self, v1, v2):
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            elif edge.v1 == v2 and edge.v2 == v1:
                return edge
        return None

    def get_adjacent_edges(self, vertex: Vertex):
        return [edge for edge in self.edges if edge.v1 == vertex or edge.v2 == vertex]

    def num_vertices(self):
        return len(self.vertices)
    
    def opposite(self, v, e):
        if e.v1 == v:
            w = e.v2
        elif e.v2 == v:
            w = e.v1
        else:
            w = None
        
        return w