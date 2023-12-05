filename: bi-startingNode-endingNode-probability-minCap-maxCap.txt

python -m memory_profiler FordFulkerson.py -f tests/bi-10-10-0.9-1-20.txt -s s -t t -g 1
Filename: FordFulkerson.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     40.3 MiB     40.3 MiB           1   @profile
    37                                         def fordFulkerson(graph, source, sink):
    38                                             """
    39                                             Implement the Ford-Fulkerson algorithm to find the maximum flow.
    40                                             """
    41     40.3 MiB      0.0 MiB           1       maxFlow = 0
    42     40.3 MiB      0.0 MiB           1       sourceVertex = graph.vertices[source]
    43     40.3 MiB      0.0 MiB           1       sinkVertex = graph.vertices[sink]
    44                                         
    45                                             while True:
    46                                                 # Find an augmenting path
    47     40.3 MiB      0.0 MiB          21           path = findAugmentingPath(graph, sourceVertex, sinkVertex)
    48     40.3 MiB      0.0 MiB          21           if not path:
    49     40.3 MiB      0.0 MiB           1               break
    50                                         
    51                                                 # Find the minimum residual capacity along the path
    52     40.3 MiB      0.0 MiB         180           pathFlow = min(edge.residualCapacity for edge in path)
    53     40.3 MiB      0.0 MiB          80           for edge in path:
    54                                                     # Augment the flow
    55     40.3 MiB      0.0 MiB          60               edge.augmentFlow(pathFlow)
    56                                         
    57                                                 # Add to the total max flow
    58     40.3 MiB      0.0 MiB          20           maxFlow += pathFlow
    59                                         
    60     40.3 MiB      0.0 MiB           1       return maxFlow


Maximum Flow: 76
Execution Time: 0.05529284477233887 seconds

python -m memory_profiler FordFulkerson.py -f tests/bi-50-50-0.9-1-100.txt -s s -t t -g 1
Filename: FordFulkerson.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     40.5 MiB     40.5 MiB           1   @profile
    37                                         def fordFulkerson(graph, source, sink):
    38                                             """
    39                                             Implement the Ford-Fulkerson algorithm to find the maximum flow.
    40                                             """
    41     40.5 MiB      0.0 MiB           1       maxFlow = 0
    42     40.5 MiB      0.0 MiB           1       sourceVertex = graph.vertices[source]
    43     40.5 MiB      0.0 MiB           1       sinkVertex = graph.vertices[sink]
    44                                         
    45                                             while True:
    46                                                 # Find an augmenting path
    47     40.5 MiB    -12.9 MiB         132           path = findAugmentingPath(graph, sourceVertex, sinkVertex)
    48     40.5 MiB    -12.9 MiB         132           if not path:
    49     40.1 MiB     -0.4 MiB           1               break
    50                                         
    51                                                 # Find the minimum residual capacity along the path
    52     40.5 MiB   -112.1 MiB        1179           pathFlow = min(edge.residualCapacity for edge in path)
    53     40.5 MiB    -49.8 MiB         524           for edge in path:
    54                                                     # Augment the flow
    55     40.5 MiB    -37.4 MiB         393               edge.augmentFlow(pathFlow)
    56                                         
    57                                                 # Add to the total max flow
    58     40.5 MiB    -12.5 MiB         131           maxFlow += pathFlow
    59                                         
    60     40.1 MiB      0.0 MiB           1       return maxFlow


Maximum Flow: 2656
Execution Time: 3.875213146209717 seconds

python -m memory_profiler FordFulkerson.py -f tests/bi-100-100-0.9-1-200.txt -s s -t t -g 1
Filename: FordFulkerson.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    36     41.7 MiB     41.7 MiB           1   @profile
    37                                         def fordFulkerson(graph, source, sink):
    38                                             """
    39                                             Implement the Ford-Fulkerson algorithm to find the maximum flow.
    40                                             """
    41     41.7 MiB      0.0 MiB           1       maxFlow = 0
    42     41.7 MiB      0.0 MiB           1       sourceVertex = graph.vertices[source]
    43     41.7 MiB      0.0 MiB           1       sinkVertex = graph.vertices[sink]
    44                                         
    45                                             while True:
    46                                                 # Find an augmenting path
    47     41.7 MiB  -4484.0 MiB         268           path = findAugmentingPath(graph, sourceVertex, sinkVertex)
    48     41.7 MiB  -4484.0 MiB         268           if not path:
    49      6.4 MiB    -35.3 MiB           1               break
    50                                         
    51                                                 # Find the minimum residual capacity along the path
    52     41.7 MiB -40041.4 MiB        2403           pathFlow = min(edge.residualCapacity for edge in path)
    53     41.7 MiB -17798.7 MiB        1068           for edge in path:
    54                                                     # Augment the flow
    55     41.7 MiB -13349.1 MiB         801               edge.augmentFlow(pathFlow)
    56                                         
    57                                                 # Add to the total max flow
    58     41.7 MiB  -4449.8 MiB         267           maxFlow += pathFlow
    59                                         
    60      6.4 MiB      0.0 MiB           1       return maxFlow


Maximum Flow: 10155
Execution Time: 56.4921977519989 seconds