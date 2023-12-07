# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Bipartite/bi-10-10-0.9-1-20.txt -s s -t t -g 1
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Bipartite/bi-50-50-0.9-1-100.txt -s s -t t -g 1
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Bipartite/bi-100-100-0.9-1-200.txt -s s -t t -g 1
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Bipartite/bi-1000-1000-0.9-1-2000.txt -s s -t t -g 1
# run fixed degree graphs
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v20-d3-min1-max20.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v20-d10-min1-max20.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v100-d3-min1-max100.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v100-d10-min1-max100.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v100-d99-min1-max100.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v200-d3-min1-max200.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v200-d10-min1-max200.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v200-d99-min1-max200.txt -s s -t t -g 2
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v1000-d3-min1-max1000.txt -s s -t t -g 2
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v1000-d10-min1-max1000.txt -s s -t t -g 2
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/FixedDegree/fix-v1000-d99-min1-max1000.txt -s s -t t -g 2
# run mesh graphs
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Mesh/3x4-max2.txt -s s -t t -g 3
python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Mesh/10x20-max10.txt -s s -t t -g 3
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Mesh/50x80-max40.txt -s s -t t -g 3
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Mesh/200x100-max100.txt -s s -t t -g 3
# python3 ./fordFulkerson/FordFulkerson.py -f ./testGraphs/Mesh/300x300-max1.txt -s s -t t -g 3