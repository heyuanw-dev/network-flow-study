# Ford-Fulkerson implementation
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
import argparse

def find_augmenting_path(graph, source, sink, path=[], visited=None):
    if visited is None:
        visited = set()

    if source == sink:
        return path

    visited.add(source)

    for edge in graph.get_adjacent_edges(source):
        residual = edge.residual_capacity
        if residual > 0 and edge not in path and edge.v2 not in visited:
            result = find_augmenting_path(graph, edge.v2, sink, path + [edge], visited)
            if result is not None:
                return result

    return None

def ford_fulkerson(graph, source, sink):
    max_flow = 0
    source_vertex = graph.vertices[source]
    sink_vertex = graph.vertices[sink]

    while True:
        path = find_augmenting_path(graph, source_vertex, sink_vertex)
        if not path:
            break

        path_flow = min(edge.residual_capacity for edge in path)
        for edge in path:
            edge.augment_flow(path_flow)

        max_flow += path_flow

    return max_flow


def main():
    parser = argparse.ArgumentParser(description="Ford-Fulkerson algorithm for maximum flow calculation.")
    parser.add_argument("file_path", help="Path to the graph input file.")
    parser.add_argument("source", help="The source vertex in the graph.")
    parser.add_argument("sink", help="The sink vertex in the graph.")

    args = parser.parse_args()

    # Create the graph and load data from the specified file
    G = SimpleGraph()
    GraphInput.load_simple_graph(G, args.file_path)

    # Calculate the maximum flow
    max_flow = ford_fulkerson(G, args.source, args.sink)
    print("Max flow:", max_flow)

if __name__ == "__main__":
    main()