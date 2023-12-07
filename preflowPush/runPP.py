import os
import time
import pandas as pd
from preflowPush import PreflowPushGraph

# Assuming PreflowPushGraph and necessary classes are defined above this code

# Function to run preflow push algorithm on a given graph file
def run_preflow_push(filePath):
    graph = PreflowPushGraph()
    graph.load_simple_graph(filePath)
    start_time = time.time()
    max_flow = graph.preflow_push()
    end_time = time.time()
    return end_time - start_time, max_flow

# Directory to search for graph files
directory = '../graphGenerationCode/testBi/bi-c/'
pp_results_df = pd.DataFrame(columns=['PP-runtime', 'PP-maxflow'])

# Iterate through files and run Preflow Push
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        runtime, maxflow = run_preflow_push(file_path)
        # startingNode = int(filename.split('-')[5])
        int_txt_part = filename.split('-')[5]
        startingNode = int_txt_part.split('.')[0]
        pp_results_df.loc[startingNode] = [runtime, maxflow]

# Convert index to integer and sort the DataFrame
pp_results_df.index = pp_results_df.index.astype(int)
pp_results_df.sort_index(inplace=True)

# Display the results
print(pp_results_df)

pp_results_df.to_csv('../csvs/preflowdf-c.csv')
