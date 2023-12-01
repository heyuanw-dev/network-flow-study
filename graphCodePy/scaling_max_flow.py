from edge import Edge
from vertex import Vertex
from simple_graph import SimpleGraph
from graph_input import GraphInput


'''Returns true if there is a path from source 's' to sink 't' in
residual graph. Also fills parent[] to store the path '''
def BFS(graph: SimpleGraph, s: Vertex, t: Vertex, parent: map, parent_name):
    visited = set()

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited.add(s)

    # Standard BFS Loop
    while queue:
 
        # Dequeue a vertex from queue and print it
        u = queue.pop(0)
        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for e in u.out_edge_list:
            ind = graph.opposite(u, e)
            val = e.capacity
            if ind not in visited and val > 0:
                # If we find a connection to the sink node, 
                # then there is no point in BFS anymore
                # We just have to set its parent and can return true
                queue.append(ind)
                visited.add(ind)
                parent[ind] = u
                parent_name[ind.name] = u.name
                if ind == t:
                    return True

    # We didn't reach sink in BFS starting 
    # from source, so return false
    return False
			
	
	# Returns the maximum flow from s to t in the given graph
def scaling_ff(graph: SimpleGraph, source: Vertex, sink: Vertex) -> int:

    # This array is filled by BFS and to store path
    parent = {}
    parent_name = {}

    max_flow = 0 # There is no flow initially

    # Augment the flow while there is path from source to sink
    while BFS(graph, source, sink, parent, parent_name) :
        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while(s != source):
            edge = graph.get_edge(parent[s], s)
            path_flow = min(path_flow, edge.capacity)
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while(v != source):
            u = parent[v]
            edge_uv = graph.get_edge(u, v)
            edge_uv.augment_flow(path_flow)
            edge_uv.capacity = edge_uv.capacity - path_flow

            edge_vu = graph.get_edge(v, u)
            if edge_vu is None:
                graph.insert_edge(v, u, path_flow)
            else:
                edge_vu.capacity = edge_vu.capacity + path_flow

            v = parent[v]

        parent.clear()


    return max_flow



G = SimpleGraph()
GraphInput.load_simple_graph(G, './graphGenerationCode/Random/n10-m10-cmin5-cmax10-f30.txt')

print ("The maximum possible flow is %d " % scaling_ff(G, G.source, G.sink))
