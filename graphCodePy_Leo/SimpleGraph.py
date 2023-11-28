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

    def insert_edge(self, v1, v2, capacity, name=None):
        edge = Edge(v1, v2, capacity, name)
        self.edges.append(edge)

    def find_edge(self, v1, v2):
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
        return None

    def get_adjacent_edges(self, vertex):
        return [edge for edge in self.edges if edge.v1 == vertex or edge.v2 == vertex]
