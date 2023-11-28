# edge.py

class Vertex:
    def __init__(self, name):
        self.name = name

class Edge:
    def __init__(self, v1, v2, capacity, name=None):
        self.v1 = v1
        self.v2 = v2
        self.capacity = capacity
        self.flow = 0
        self.name = name

    @property
    def residual_capacity(self):
        return self.capacity - self.flow

    def augment_flow(self, additional_flow):
        self.flow += additional_flow
