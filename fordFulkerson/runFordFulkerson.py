import os
import pandas as pd
import time
from SimpleGraph import SimpleGraph
from GraphInput import GraphInput
from FordFulkerson import fordFulkerson, parseGraph
import argparse

# Parse command line arguments for input and output directories
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Input directory containing graph files.')
parser.add_argument('output_dir', help='Output directory for CSV file.')
args = parser.parse_args()

def runFordFulkerson(filePath):
    G = SimpleGraph()
    parseGraph(G, filePath)
    startTime = time.time()
    maxFlow = fordFulkerson(G, 's', 't')  # source is 's', sink is 't'
    endTime = time.time()

    return endTime - startTime, maxFlow

# List all files in the input directory
files = os.listdir(args.input_dir)

# DataFrame to store results
results_df = pd.DataFrame(columns=['Filename', 'FF-runtime', 'FF-maxflow'])

# Iterate through files and run Ford-Fulkerson
index = 0
for file in sorted(os.listdir(args.input_dir)):
    if file.endswith('.txt'):
        filePath = os.path.join(args.input_dir, file)
        runtime, maxflow = runFordFulkerson(filePath)
        results_df.loc[index] = [file, runtime, maxflow]
        index += 1


# print(results_df)
# Output result to output directory
results_df.to_csv(os.path.join(args.output_dir, 'ff-bipartite-t.csv'))
