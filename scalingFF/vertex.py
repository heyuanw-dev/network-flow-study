class Vertex:
    def __init__(self, name: str, data=None):
        self.name = name
        self.data = data
        self.out_edge_list = []
        self.in_edge_list = []

    def __str__(self) -> str:
        return str(self.name)