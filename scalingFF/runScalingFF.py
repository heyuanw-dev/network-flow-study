import os
import pandas as pd
import time
from scaling_max_flow import scaling_ff
from simple_graph import SimpleGraph
from graph_input import GraphInput
import argparse

# Parse command line arguments for input and output directories
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Input directory containing graph files.')
parser.add_argument('output_dir', help='Output directory for CSV file.')
args = parser.parse_args()

def runScalingFF(filePath):
    G = SimpleGraph()
    GraphInput.load_simple_graph(G, filePath)

    start_time = time.time()
    max_flow = scaling_ff(G, G.source, G.sink)
    end_time = time.time()
    runtime = end_time - start_time


    return runtime, max_flow

# DataFrame to store results
results_df = pd.DataFrame(columns=['Filename', 'SFF-runtime', 'SFF-maxflow'])

# Check if the input directory exists
if os.path.exists(args.input_dir) and os.path.isdir(args.input_dir):
    index = 0
    for filename in sorted(os.listdir(args.input_dir)):
        if filename.endswith('.txt'):
            file_path = os.path.join(args.input_dir, filename)
            runtime, max_flow = runScalingFF(file_path)
            results_df.loc[index] = [filename, runtime, max_flow]
        index += 1

# Convert index to integer and sort the DataFrame
results_df.index = results_df.index.astype(int)
results_df.sort_index(inplace=True)
# print(results_df)

# Output results to the specified output directory
results_df.to_csv(os.path.join(args.output_dir, 'scaling-t.csv'))
