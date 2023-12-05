from edge import Edge
from vertex import Vertex
from simple_graph import SimpleGraph
from graph_input import GraphInput
import math, os, time


'''Returns true if there is a path from source 's' to sink 't' in
residual graph. Also fills parent[] to store the path '''
def DFS(graph: SimpleGraph, s: Vertex, t: Vertex, parent: map, delta: int):
    visited = set()

    # Create a stack for DFS
    stack = []

    # Mark the source node as visited and enqueue it
    stack.append(s)
    visited.add(s)

    # Standard DFS Loop
    while stack:
 
        # Dequeue a vertex from queue and print it
        u = stack.pop()
        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for e in u.out_edge_list:
            ind = graph.opposite(u, e)
            val = e.capacity
            if ind not in visited and val >= delta:
                # If we find a connection to the sink node, 
                # then there is no point in DFS anymore
                # We just have to set its parent and can return true
                stack.append(ind)
                visited.add(ind)
                parent[ind] = u
                if ind == t:
                    return True

    # We didn't reach sink in DFS starting from source, so return false
    return False
			
	
	# Returns the maximum flow from s to t in the given graph
def scaling_ff(graph: SimpleGraph, source: Vertex, sink: Vertex) -> int:

    # This array is filled by DFS and to store path
    parent = {}

    max_flow = 0 # There is no flow initially

    delta = 2 ** math.floor(math.log(graph.max_capacity, 2))

    while (delta >= 1):
    # Augment the flow while there is path from source to sink
        while DFS(graph, source, sink, parent, delta) :
            # Find minimum residual capacity of the edges along the
            # path filled by DFS. Or we can say find the maximum flow
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

        delta = delta / 2

    return max_flow


if __name__ == "__main__":

    G = SimpleGraph()

    # Ask the user for the folder path
    folder_path = input("Enter the folder path: ")

    runtime_results = []
    flow_results = []

    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Iterate through the files in the folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            GraphInput.load_simple_graph(G, file_path)
            # Measure the execution time of the function
            start_time = time.time()
            flow = scaling_ff(G, G.source, G.sink)
            end_time = time.time()
            # Calculate and print the elapsed time
            elapsed_time = end_time - start_time
            flow_results.append(flow)
            runtime_results.append(elapsed_time)
            print(elapsed_time)
    else:
        print(f"Folder '{folder_path}' does not exist.")

    print(flow_results)
    print(runtime_results)
