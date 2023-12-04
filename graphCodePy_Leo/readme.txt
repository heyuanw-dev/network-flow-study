Structure for input:

python FordFulkerson.py -f (file path) -s (starting node) -t (ending node) -g (graph type)

For -s and -t, normally we just use s and t, so:

-s s -t t

For graph type, 1 = Bipartite, 2 = Fixed Degree, 3 = Mesh, 4 = Random Graph.

Example for test running:

Bipartite:
python .\FordFulkerson.py -f .\tests\g1.txt -s s -t t -g 1
python .\FordFulkerson.py -f .\tests\g2.txt -s s -t t -g 1

Fixed Degree:
python .\FordFulkerson.py -f .\tests\20v-3out-4min-355max.txt -s s -t t -g 2
python .\FordFulkerson.py -f .\tests\100v-5out-25min-200max.txt -s s -t t -g 2

Mesh:
python .\FordFulkerson.py -f .\tests\smallMesh.txt -s s -t t -g 3
python .\FordFulkerson.py -f .\tests\mediumMesh.txt -s s -t t -g 3

Random:
python .\FordFulkerson.py -f .\tests\n10-m10-cmin5-cmax10-f30.txt -s s -t t -g 4
python .\FordFulkerson.py -f .\tests\n100-m100-cmin10-cmax20-f949.txt -s s -t t -g 4