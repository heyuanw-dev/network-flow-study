# Import necessary modules
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
import argparse

def findAugmentingPath(graph, source, sink, path=[], visited=None):
    """
    Find an augmenting path in the graph from source to sink.
    """
    # Initialize visited set if not provided
    if visited is None:
        visited = set()

    # Return the path if source and sink are the same
    if source == sink:
        return path

    # Mark the source as visited
    visited.add(source)

    # Explore adjacent edges
    for edge in graph.getAdjacentEdges(source):
        # Check for residual capacity
        residual = edge.residualCapacity
        if residual > 0 and edge not in path and edge.v2 not in visited:
            # Recursively find path from the next vertex
            result = findAugmentingPath(graph, edge.v2, sink, path + [edge], visited)
            if result is not None:
                return result

    # No augmenting path found
    return None

def fordFulkerson(graph, source, sink):
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow.
    """
    maxFlow = 0
    sourceVertex = graph.vertices[source]
    sinkVertex = graph.vertices[sink]

    while True:
        # Find an augmenting path
        path = findAugmentingPath(graph, sourceVertex, sinkVertex)
        if not path:
            break

        # Find the minimum residual capacity along the path
        pathFlow = min(edge.residualCapacity for edge in path)
        for edge in path:
            # Augment the flow
            edge.augmentFlow(pathFlow)

        # Add to the total max flow
        maxFlow += pathFlow

    return maxFlow

def parseGraph(graph, filePath):
    """
    General function to parse graph from a given file.
    """
    with open(filePath, 'r') as file:
        for line in file:
            fromVertex, toVertex, capacity = line.split()
            # Insert vertices and edge into the graph
            v1 = graph.insertVertex(fromVertex)
            v2 = graph.insertVertex(toVertex)
            graph.insertEdge(v1, v2, int(capacity))

def calculateGraphDensity(graph):
    """
    Calculate and print the density of the graph.
    """
    numVertices = graph.numVertices()
    numEdges = len(graph.edges)
    density = numEdges / (numVertices * (numVertices - 1)) if numVertices > 1 else 0
    print(f"Density of the Graph: {density:.4f}")

def main():
    """
    Main function to execute the program.
    """
    parser = argparse.ArgumentParser(description="Calculate max flow using Ford-Fulkerson algorithm.")

    # Define command line arguments
    parser.add_argument("-f", "--filePath", required=True, help="Path to the graph input file.")
    parser.add_argument("-s", "--source", required=True, help="Source vertex in the graph.")
    parser.add_argument("-t", "--sink", required=True, help="Sink vertex in the graph.")
    parser.add_argument("-g", "--graphType", type=int, choices=[1, 2, 3, 4], required=True, help="Type of graph: 1-Bipartite, 2-Fixed Degree, 3-Mesh, 4-Random.")

    args = parser.parse_args()

    # Create a graph instance
    G = SimpleGraph()

    # Parse the graph based on the input file
    parseGraph(G, args.filePath)

    # Calculate the maximum flow
    maxFlow = fordFulkerson(G, args.source, args.sink)
    print("Maximum Flow:", maxFlow)

    # Optional: Calculate graph density for random graphs
    if args.graphType == 4:
        calculateGraphDensity(G)

if __name__ == "__main__":
    main()
