import os
import pandas as pd
import time
from preflowPush import PreflowPushGraph
import argparse

# Parse command line arguments for input and output directories
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Input directory containing graph files.')
parser.add_argument('output_dir', help='Output directory for CSV file.')
args = parser.parse_args()

def run_preflow_push(filePath):
    graph = PreflowPushGraph()
    graph.load_simple_graph(filePath)
    start_time = time.time()
    max_flow = graph.preflow_push()
    end_time = time.time()
    return end_time - start_time, max_flow

# DataFrame to store results
pp_results_df = pd.DataFrame(columns=['Filename', 'PP-runtime', 'PP-maxflow'])

# Check if the input directory exists
if os.path.exists(args.input_dir) and os.path.isdir(args.input_dir):
    index = 0
    for filename in sorted(os.listdir(args.input_dir)):
        if filename.endswith('.txt'):
            file_path = os.path.join(args.input_dir, filename)
            runtime, maxflow = run_preflow_push(file_path)
            pp_results_df.loc[index] = [filename, runtime, maxflow]
            index += 1

# Convert index to integer and sort the DataFrame
pp_results_df.index = pp_results_df.index.astype(int)
pp_results_df.sort_index(inplace=True)
# print(pp_results_df)

# Output results to the specified output directory
pp_results_df.to_csv(os.path.join(args.output_dir, 'preflowdf-t.csv'))
