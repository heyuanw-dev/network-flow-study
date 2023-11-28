# Example integration
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
from FordFulkerson import ford_fulkerson
# Create the graph and load data
G = SimpleGraph()
GraphInput.load_simple_graph(G, 'graph_data.txt')

# Calculate the maximum flow
max_flow = ford_fulkerson(G, 'S', 'T')
print("Max flow:", max_flow)
