# Python program for implementation 
# of Ford Fulkerson algorithm
from edge import *
from SimpleGraph import *
from GraphInput import *

'''Returns true if there is a path from source 's' to sink 't' in
residual graph. Also fills parent[] to store the path '''

def BFS(graph, s, t, parent):

    visited = {}

    # Create a queue for BFS
    queue = []

    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    # Standard BFS Loop
    while queue:

        # Dequeue a vertex from queue and print it
        u = queue.pop(0)
        print("CURRENT NODE: " + u)
        u = graph.vertices[u]
        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for e in graph.get_adjacent_edges(u):
            ind = graph.opposite(u, e)
            val = e.capacity
            if not ind.name in visited and val > 0:
                # If we find a connection to the sink node, 
                # then there is no point in BFS anymore
                # We just have to set its parent and can return true
                queue.append(ind.name)
                visited[ind.name] = True
                parent[ind.name] = u.name
                if ind.name == t:
                    return True

    # We didn't reach sink in BFS starting 
    # from source, so return false
    return False
			
	
	# Returns the maximum flow from s to t in the given graph
def FordFulkerson(graph: SimpleGraph, source: Vertex, sink: Vertex) -> int:

    # This array is filled by BFS and to store path
    parent = {}

    max_flow = 0 # There is no flow initially

    # Augment the flow while there is path from source to sink
    while BFS(graph, source, sink, parent) :
        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while(s != source):
            print(s)
            print(parent[s])
            edge = graph.find_edge(graph.vertices[parent[s]], graph.vertices[s])
            path_flow = min (path_flow, edge.capacity)
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while(v != source):
            u = parent[v]
            # self.graph[u][v] -= path_flow
            # self.graph[v][u] += path_flow
            edge_uv = graph.find_edge(graph.vertices[u], graph.vertices[v])
            edge_uv.augment_flow(path_flow)
            edge_uv.capacity = edge_uv.capacity - path_flow

            edge_vu = graph.find_edge(v, u)
            if edge_vu is None:
                graph.insert_edge(v, u, path_flow)
            else:
                edge_vu.capacity = edge_vu.capacity + path_flow

            v = parent[v]

    return max_flow



G = SimpleGraph()
GraphInput.load_simple_graph(G, './graphCodePy_Leo/graph_data.txt')

print ("The maximum possible flow is %d " % FordFulkerson(G, 'S', 'T'))
