
from edge import Vertex, Edge

class SimpleGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def insertVertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name)
        return self.vertices[name]

    def insertEdge(self, v1: Vertex, v2: Vertex, capacity, name=None):
        edge = Edge(v1, v2, capacity, name)
        self.edges.append(edge)

    def findEdge(self, v1, v2):
        for edge in self.edges:
            if edge.v1 == v1 and edge.v2 == v2:
                return edge
            elif edge.v1 == v2 and edge.v2 == v1:
                return edge
        return None

    def getAdjacentEdges(self, vertex: Vertex):
        return [edge for edge in self.edges if edge.v1 == vertex or edge.v2 == vertex]

    def numVertices(self):
        return len(self.vertices)
    
    def opposite(self, v, e):
        if e.v1 == v:
            w = e.v2
        elif e.v2 == v:
            w = e.v1
        else:
            w = None
        
        return w

    def calculateDensity(self):
        numVertices = len(self.vertices)
        numEdges = len(self.edges)
        if numVertices > 1:
            maxEdges = numVertices * (numVertices - 1)
            return numEdges / maxEdges
        else:
            return 0
