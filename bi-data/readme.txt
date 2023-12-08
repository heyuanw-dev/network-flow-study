These are generated dataset for bipartite graph.
parameters:

ff-bipartite: runtime & maxflow for FordFulkerson.
scaling: runtime & maxflow for scaling FordFulkerson
preflowdf: runtime & maxflow for preflow push

-c: change on max capacity
-m: change on right node
-p: change on probability.

The code for generating these graphs is located on graphGenerationCode\testBi. This is a modified version based on the code provided.

The following is the description of each folder of graphs.
bi-c: change on max capacity +=10(1~101)
bi-m: change on right node +=10(1~101)
bi-n: change on left node +=10(1~101)
bi-p: change on probability +=0.1(0.1~1)
bi-nm1~100: change on both left and right node +=1 (1~100)