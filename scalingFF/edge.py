from vertex import Vertex

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, data: int, name=None):
        self.v1 = v1
        self.v2 = v2
        self.capacity = data
        self.flow = 0
        self.name = name

    def augment_flow(self, flow_value):
        self.flow += flow_value

    def __str__(self):
        """
        Return a string representation of the edge.
        """
        if self.flow is not None:
            return f"({self.v1} -> {self.v2}, flow={self.flow})"
        else:
            return f"({self.v1} -> {self.v2})"