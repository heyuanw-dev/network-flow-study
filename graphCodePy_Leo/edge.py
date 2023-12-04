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

    @property
    def residualCapacity(self):
        return self.capacity - self.flow

    def augmentFlow(self, additionalFlow):
        self.flow += additionalFlow