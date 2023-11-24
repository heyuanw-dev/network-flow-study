class Vertex:
    # Assuming a basic Vertex class implementation
    pass

class Edge:
    def __init__(self, v1, v2, data=None, name=None):
        self.v1 = v1
        self.v2 = v2
        self.data = data
        self.name = name

    @property
    def first_endpoint(self):
        return self.v1

    @property
    def second_endpoint(self):
        return self.v2

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
