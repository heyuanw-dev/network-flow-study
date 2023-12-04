from SimpleGraph import Edge, Vertex
import os

# Implementation of the preflow-push algorithm for the maximum flow problem
# Vertex class inherited from given Vertex with height and excess attributes
# height: height of the vertex
# excess: excess of the vertex
# adjacent_vertices: list of adjacent vertices
class HeightVertex(Vertex):
    def __init__(self, name: str, height: int =0, excess: float =0, data=None):
        super().__init__(data, name)
        self.height = height
        self.excess = excess
        self.adjacent_vertices: list[str] = []
    def is_source(self):
        return self.name == "s"
    def is_sink(self):
        return self.name == "t"

# Edge class inherited from given Edge with flow and capacity attributes   
class PreflowPushEdge(Edge):
    def __init__(self, v1, v2, capacity: float, flow: float =0, name=None):
        super().__init__(v1, v2, capacity, name)
        self.flow = flow
        self.capacity = capacity

# Graph class for preflow-push algorithm, that contains vertices and edges
# Vertices are stored in a dictionary with name as key and HeightVertex as value
# Edges are stored in a dictionary with tuple of (v1, v2) as key and PreflowPushEdge as value
# source and sink are stored as HeightVertex
class PreflowPushGraph():

    def __init__(self):
        self.source: HeightVertex = None # source of the graph
        self.sink: HeightVertex = None # sink of the graph
        self.vertices: dict[str, HeightVertex] = {} # set of vertices
        self.edges: dict[tuple, PreflowPushEdge] = dict() # dictionary of edges
    
    # Graph construction
    # Construct a HeightVertex class with a name of the node and added to the vertices dictionary
    # name: name of the vetex
    # Return created vertex
    def insert_vertex(self, name):
        vertex = HeightVertex(name)
        if name == "s":
            self.source = vertex
        elif name == "t":
            self.sink = vertex
        self.vertices[name] = vertex
        return vertex
    
    # Construct a PreflowPushEdge class with a name of the edge and added to the edges dictionary
    # Backward edge will be represented by a negative flow and capacity of 0
    # v1: starting node
    # v2: ending node
    # capacity: capacity of the edge
    # flow: flow of the edge
    # Return created edge
    def insert_edge(self, v1, v2, capacity, flow=0):
        edge = PreflowPushEdge(v1, v2, capacity, flow)
        self.edges[(v1, v2)] = edge
        self.vertices[v1].adjacent_vertices.append(v2)
        return edge
    # Get number of vertices and edges
    def num_vertices(self):
        return len(self.vertices)
    def num_edges(self):
        return len(self.edges)
    
    # Load a graph from a txt file, extended from
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
                    # insert vertices  if not already in the graph, tracked with a dictionary
                    v1 = self.vertices.get(v1name) or self.insert_vertex(v1name)
                    v2 = self.vertices.get(v2name) or self.insert_vertex(v2name)
                    # insert edge
                    self.insert_edge(v1name, v2name, edge_capacity)
                else:
                    print(f"Error: Invalid number of tokens found on line {line_count}!")
                    return None
        
        print(f"Successfully loaded {line_count} lines.")
        return table
        
    ######## Algorithm implementation ########

    def push(self, v: HeightVertex, w: HeightVertex):
        # Push flow from node v to node w
        vw_edge = self.edges[(v.name, w.name)]
        # find minimum among excess of v and the possible residual flow of edge (v,w) 
        flow_to_push = min(v.excess, vw_edge.capacity - vw_edge.flow)
        # update flow of edge (v,w) and (w,v)
        vw_edge.flow += flow_to_push 
        # update backward edge with negative flow from w to v, if not in graph, insert it
        if self.edges.get((w.name, v.name)) is not None:
            self.edges[(w.name,v.name)].flow -= flow_to_push
        else:
            self.insert_edge(w.name, v.name, 0, -flow_to_push)
        # update excess of v and w
        # reduce excess of v by flow_to_push, and increase excess of w by flow_to_push
        v.excess -= flow_to_push
        w.excess += flow_to_push

    # Relabel the height of node v, increment height of v by 1 each time
    def relabel(self, v: HeightVertex):
        # Relabel the height of node v
        v.height += 1 

    # Get all active nodes, which are nodes with positive excess and not source or sink
    # Return a list of HeightVertex
    def getActiveNodes(self):
        return [v for v in self.vertices.values() if not v.is_sink() and not v.is_source() and v.excess > 0]

    # Preflow-push algorithm on loaded graph represented by vertices and edges
    # Return: maximum flow
    def preflow_push(self):
        # Initialize preflow
        # Check if source and sink are defined, report error if not
        if self.source is None or self.sink is None:
            print("Error: Source or sink not defined!")
            return None
        # Initialize a pre-flow by setting height of source to |V| and excess of source to infinity
        # initialize a preflow saturating all edges out from source
        # height of source is |V|
        self.source.height = self.num_vertices()
        # excess of source is infinity
        self.source.excess = float("inf")
        # set source node name 's'
        sourceName = self.source.name
        # saturate all edges out from source
        for v in self.source.adjecent_vertices:
            # flow from source to v is equal to capacity
            self.edges[(sourceName, v)].flow = self.edges[(sourceName, v)].capacity 
            # create backward edge as negative flow from v to source
            self.insert_edge(v, sourceName, capacity=0, flow=-self.edges[(sourceName, v)].capacity)
            # update excess of v equal to capacity of edge (source, v)
            self.vertices[v].excess = self.edges[(sourceName, v)].capacity  
            # update excess of source by reducing it by capacity of edge (source, v)
            self.source.excess -= self.edges[(sourceName, v)].capacity
        
        # excess of source should be 0 after pushing all flow out from source
        self.source.excess = 0
        # Initialize active nodes with positive excess
        activeNodes = self.getActiveNodes()

        # Main loop checkin if there are active nodes, and apply push() or relabel() accordingly
        while len(activeNodes) != 0:
            vert: HeightVertex = activeNodes[0]
            found_push = False
            # check adjacent nodes of the selected node, if there is a node with positive excess and height less than the selected node, push flow to that node
            for v_name in vert.adjacent_vertices:
                v = self.vertices.get(v_name)
                if vert.excess > 0 and (vert.height > v.height ) and self.edges[(vert.name, v.name)].capacity > self.edges[(vert.name, v.name)].flow :
                    self.push(vert, v) # apply push
                    found_push = True
                    break
                
            if not found_push:
                # relabel selected node if push is not applicable
                self.relabel(vert)
            # update nodes with positive excess
            activeNodes = self.getActiveNodes() 
        # Calculate the maximum flow by summation of all flows left from source
        max_flow = sum([self.edges[(self.source.name, v)].flow for v in self.source.adjacent_vertices])
        return max_flow
    

# Test cases
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