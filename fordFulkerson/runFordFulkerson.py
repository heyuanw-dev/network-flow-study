import os
import pandas as pd
import time
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
from FordFulkerson import fordFulkerson, parseGraph
import argparse
import time
def runFordFulkerson(filePath):
    G = SimpleGraph()
    parseGraph(G, filePath)  # Assuming parseGraph function is already defined
    startTime = time.time()
    maxFlow = fordFulkerson(G, 's', 't')  # source is 's', sink is 't'
    endTime = time.time()

    return endTime - startTime, maxFlow

# List all files in the directory
directory = '../graphGenerationCode/testBi/bi-demo/'
files = os.listdir(directory)

# DataFrame to store results
results_df = pd.DataFrame(columns=['FF-runtime', 'FF-maxflow'])

# Iterate through files and run Ford-Fulkerson
for file in files:
    if file.endswith('.txt'):
        filePath = os.path.join(directory, file)
        # int_txt_part = file.split('-')[5]
        # startingNode = int_txt_part.split('.')[0]  # Extract starting node number from the file name
        startingNode = file.split('-')[1]

        runtime, maxflow = runFordFulkerson(filePath)
        results_df.loc[startingNode] = [runtime, maxflow]  # Use starting node as row ID

# Display the results
print(results_df)
results_df.to_csv('../csvs/ff-bipartite-t.csv')