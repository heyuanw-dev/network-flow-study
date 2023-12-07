# edge.py

class Vertex:
    def __init__(self, name):
        self.name = name
        self.incident_edges = []

    def __str__(self) -> str:
        return str(self.name)


class Edge:
    def __init__(self, v1, v2, capacity, name=None):
        self.v1 = v1
        self.v2 = v2
        self.capacity = capacity
        self.flow = 0
        self.name = name
        self.backEdge = None  # New attribute for the back edge

    @property
    def residualCapacity(self):
        return self.capacity - self.flow

    def augmentFlow(self, additionalFlow):
        self.flow += additionalFlow
        # Update the flow of the back edge
        if self.backEdge:
            self.backEdge.flow -= additionalFlow