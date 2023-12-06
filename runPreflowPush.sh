# run bipartite graphs
python3 preflowPush/preflowPush.py "./testGraphs/Bipartite/bi-10-10-0.9-1-20.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Bipartite/bi-50-50-0.9-1-100.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Bipartite/bi-100-100-0.9-1-200.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Bipartite/bi-1000-1000-0.9-1-2000.txt"

# run fixed degree
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v20-d3-min1-max20.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v100-d3-min1-max100.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v200-d3-min1-max200.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v1000-d3-min1-max1000.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v20-d10-min1-max20.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v100-d10-min1-max100.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v200-d10-min1-max200.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v1000-d10-min1-max1000.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v100-d99-min1-max100.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v200-d99-min1-max200.txt"
python3 preflowPush/preflowPush.py "./testGraphs/FixedDegree/fix-v1000-d99-min1-max1000.txt"

# run mesh graphs
python3 preflowPush/preflowPush.py "./testGraphs/Mesh/3x4-max2.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Mesh/10x20-max10.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Mesh/50x80-max40.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Mesh/200x100-max100.txt"
python3 preflowPush/preflowPush.py "./testGraphs/Mesh/300x300-max1.txt"