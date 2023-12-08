import os
import pandas as pd
import time
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
from FordFulkerson import fordFulkerson, parseGraph
import argparse
import time
# File for executing ford fulkerson's algorithm for all the files in a directory, and output as a csv dataset with runtime & maxflow.
def runFordFulkerson(filePath):
    G = SimpleGraph()
    parseGraph(G, filePath)
    startTime = time.time()
    maxFlow = fordFulkerson(G, 's', 't')  # source is 's', sink is 't'
    endTime = time.time()

    return endTime - startTime, maxFlow

# List all files in the directory
directory = '../bi-data/bi-demo/'
files = os.listdir(directory)

# DataFrame to store results
results_df = pd.DataFrame(columns=['FF-runtime', 'FF-maxflow'])

# Iterate through files and run Ford-Fulkerson
for file in files:
    if file.endswith('.txt'):
        filePath = os.path.join(directory, file)
        # Extract the first snippet after parsing with '-'. This is for generating index keys for datasets, adjust based on your choice.
        # int_txt_part = file.split('-')[5]
        # startingNode = int_txt_part.split('.')[0]  
        startingNode = file.split('-')[1]

        runtime, maxflow = runFordFulkerson(filePath)
        results_df.loc[startingNode] = [runtime, maxflow]  # Use starting node as row ID

# Display the results
print(results_df)
# Output result to directory. 
results_df.to_csv('../csvs/ff-bipartite-t.csv')