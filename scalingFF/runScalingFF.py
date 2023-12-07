import pandas as pd
import os
import time
from scaling_max_flow import scaling_ff
from simple_graph import SimpleGraph
from graph_input import GraphInput

# Generating Visualization use only.
directory = '../graphGenerationCode/testBi/bi-demo/'
temp_results_df = pd.DataFrame(columns=['SFF-runtime', 'SFF-maxflow'])

# Check if the directory exists
if os.path.exists(directory) and os.path.isdir(directory):
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            G = SimpleGraph()
            GraphInput.load_simple_graph(G, file_path)

            start_time = time.time()
            max_flow = scaling_ff(G, G.source, G.sink)
            end_time = time.time()
            runtime = end_time - start_time
            # int_txt_part = filename.split('-')[5]
            # startingNode = int(int_txt_part.split('.')[0])
            startingNode = int(filename.split('-')[1])
            temp_results_df.loc[startingNode] = [runtime, max_flow]

# Convert index to integer and sort the temporary DataFrame
temp_results_df.index = temp_results_df.index.astype(int)
temp_results_df.sort_index(inplace=True)
print(temp_results_df)
temp_results_df.to_csv('../csvs/scaling-t.csv')