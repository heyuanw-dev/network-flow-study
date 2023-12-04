from SimpleGraph import SimpleGraph, Edge, Vertex
import os

class HeightVertex(Vertex):
    def __init__(self, name: str, height: int =0, excess: float =0, data=None):
        super().__init__(data, name)
        self.height = height
        self.excess = excess
        self.adjecent_vertices: list[str] = []
    def is_source(self):
        return self.name == "s"
    def is_sink(self):
        return self.name == "t"
    def __str__(self):
        return f"{self.name}({self.height})"
    
class PreflowPushEdge(Edge):
    def __init__(self, v1, v2, capacity: float, flow: float =0, name=None):
        super().__init__(v1, v2, capacity, name)
        self.flow = flow
        self.capacity = capacity


class PreflowPushGraph():

    def __init__(self):
        self.source: HeightVertex = None
        self.sink: HeightVertex = None
        self.vertices: dict[str, HeightVertex] = {}
        self.edges: dict[tuple, PreflowPushEdge] = dict()
    
    def insert_vertex(self, name):
        vertex = HeightVertex(name)
        if name == "s":
            self.source = vertex
        elif name == "t":
            self.sink = vertex
        self.vertices[name] = vertex
        #self.vertiex_list.append(vertex)
        return vertex
    def insert_edge(self, v1, v2, capacity, flow=0):
        edge = PreflowPushEdge(v1, v2, capacity, flow)
        self.edges[(v1, v2)] = edge
        self.vertices[v1].adjecent_vertices.append(v2)
        #self.edge_list.append(edge)
        #v1.incident_edge_list.append(edge)
        #v2.incident_edge_list.append(edge)
        return edge
    def insert_backward_edge(self, v1, v2, capacity):
        self.edges[(v2, v1)] = PreflowPushEdge(v2, v1, capacity)
        return
    def num_vertices(self):
        return len(self.vertices)
    def num_edges(self):
        return len(self.edges)
    
    def load_simple_graph(self, pathandfilename):
        if not os.path.exists(pathandfilename):
            print(f"File {pathandfilename} not found")
            return None

        table = {}
        line_count = 0

        with open(pathandfilename, 'r') as file:
            for line in file:
                line_count += 1
                tokens = line.split()

                if len(tokens) == 3:
                    v1name, v2name, edge_capacity = tokens
                    edge_capacity = float(edge_capacity)

                    v1 = self.vertices.get(v1name) or self.insert_vertex(v1name)
                    v2 = self.vertices.get(v2name) or self.insert_vertex(v2name)

                    #table[v1name] = v1
                    #table[v2name] = v2

                    self.insert_edge(v1name, v2name, edge_capacity)
                    #self.insert_backward_edge(v1name, v2name, 0)
                else:
                    print(f"Error: Invalid number of tokens found on line {line_count}!")
                    return None
        
        print(f"Successfully loaded {line_count} lines.")
        return table
        
    # Algorithm implementation

    def push(self, v: HeightVertex, w: HeightVertex):
        # Push flow from node v to node w
        vw_edge = self.edges[(v.name, w.name)]
        flow_to_push = min(v.excess, vw_edge.capacity - vw_edge.flow)
        vw_edge.flow += flow_to_push
        if self.edges.get((w.name, v.name)) is not None:
            self.edges[(w.name,v.name)].flow -= flow_to_push
        else:
            self.insert_edge(w.name, v.name, 0, -flow_to_push)
        v.excess -= flow_to_push
        w.excess += flow_to_push

    def relabel(self, v: HeightVertex):
        # Relabel the height of node v
        v.height += 1 
    def getActiveNodes(self):
        return [v for v in self.vertices.values() if not v.is_sink() and not v.is_source() and v.excess > 0]

    def preflow_push(self):
        # Initialize preflow
        if self.source is None or self.sink is None:
            print("Error: Source or sink not defined!")
            return None
        self.source.height = self.num_vertices() # height of source is |V|
        self.source.excess = float("inf") # excess of source is infinity
        sourceName = self.source.name
        for v in self.source.adjecent_vertices:
            
            self.edges[(sourceName, v)].flow = self.edges[(sourceName, v)].capacity # flow from source to v is equal to capacity
            # update backward edge with negative flow from v to source
            self.insert_edge(v, sourceName, capacity=0, flow=-self.edges[(sourceName, v)].capacity)
            #self.edges[(v, sourceName)].flow = - self.edges[(sourceName, v)].capacity 
            self.vertices[v].excess = self.edges[(sourceName, v)].capacity  # excess of v is equal to capacity of edge (source, v)
            self.source.excess -= self.edges[(sourceName, v)].capacity
        self.source.excess = 0
        # Initialize active nodes
        activeNodes = self.getActiveNodes()

        # Push-relabel algorithm
        while len(activeNodes) != 0:
            vert: HeightVertex = activeNodes[0]
            found_push = False
            for v_name in vert.adjecent_vertices:
                v = self.vertices.get(v_name)
                if vert.excess > 0 and (vert.height > v.height ) and self.edges[(vert.name, v.name)].capacity > self.edges[(vert.name, v.name)].flow :
                    self.push(vert, v)
                    found_push = True
                    break
                
            if not found_push:
                
                
                self.relabel(vert)
            activeNodes = self.getActiveNodes()
        # Calculate the maximum flow
        max_flow = sum([self.edges[(self.source.name, v)].flow for v in self.source.adjecent_vertices])
        return max_flow
    

if __name__ == "__main__":
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Bipartite/g1.txt")
    print(graph.preflow_push() == 150)
    graph2 = PreflowPushGraph()
    graph2.load_simple_graph("../graphGenerationCode/FixedDegree/20v-3out-4min-355max.txt") 
    print(graph2.preflow_push() == 368)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Bipartite/g2.txt")
    print(graph.preflow_push() == 898)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/FixedDegree/100v-5out-25min-200max.txt")
    print(graph.preflow_push() == 517)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Random/n10-m10-cmin5-cmax10-f30.txt")
    print(graph.preflow_push() == 25)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Random/n100-m100-cmin10-cmax20-f949.txt")
    print(graph.preflow_push() == 949)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Mesh/smallMesh.txt")
    print(graph.preflow_push() == 6)
    graph = PreflowPushGraph()
    graph.load_simple_graph("../graphGenerationCode/Mesh/MediumMesh.txt")
    print(graph.preflow_push() == 39)