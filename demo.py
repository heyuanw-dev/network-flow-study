# Purpose for demoing for TCSS 543 final project.
import subprocess
import pandas as pd
import os
import platform
import psutil
import argparse
# How to use this code:
# python demo.py -i (the FOLDER for the graph txt files) -o (the folder for output dataset directories)
# e.g. python demo.py -i bi-data\bi-c -o outputData
# runFordFulkerson, runScalingFF and runPP are codes that takes folder as input and run the algorithm of each in all the folders.
# For individual graph testing, please see FordFulkerson.py, scaling_max_flow.py and preflowPush.py under each algorithms' subfolders.
# Function to parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Run graph algorithms and merge results.')
    parser.add_argument('-i', '--input_dir', required=True, help='Input directory containing graph files.')
    parser.add_argument('-o', '--output_dir', required=True, help='Output directory for CSV files.')
    return parser.parse_args()

def run_script(script_path, input_dir, output_dir):
    # Convert relative paths to absolute paths
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)
    if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    # Save the current directory
    original_dir = os.getcwd()

    # Change to the script's directory
    os.chdir(os.path.dirname(script_path))

    # Run the script with absolute paths
    subprocess.run(["python", os.path.basename(script_path), input_dir, output_dir], check=True)

    # Change back to the original directory
    os.chdir(original_dir)

def show_device_info():
    print("Device Information:")

    # Operating system
    print(f"Operating System: {platform.system()} {platform.release()}")

    # Processor
    print(f"Processor: {platform.processor()}")

    # RAM
    ram = psutil.virtual_memory()
    print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")

show_device_info()

args = parse_args()

# Paths to the Python scripts
script_paths = [
    "fordFulkerson/runFordFulkerson.py",
    "scalingFF/runScalingFF.py",
    "preflowPush/runPP.py"
]

# Execute each script
for script in script_paths:
    print('running: ', script)
    run_script(script, args.input_dir, args.output_dir)
    print('Complete executing: ', script)

# Paths to the CSV files
csv_paths = [os.path.join(args.output_dir, csv) for csv in ["ford-fulkerson.csv", "preflow-push.csv", "scaling-ff.csv"]]

# Read and merge the CSV files...
# Read and merge the CSV files. This is for displaying three algorithms' result in terminal. you can use merged_df.to_csv to output the dataset.
dfs = [pd.read_csv(csv) for csv in csv_paths]

merged_df = dfs[0]
for df in dfs[1:]:
    merged_df = pd.merge(merged_df, df, on='Filename')

# Drop any columns that are 'Unnamed'
merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]

# Ensure 'Filename' is the first column if it's not already
cols = list(merged_df.columns)
if 'Filename' in cols:
    cols.insert(0, cols.pop(cols.index('Filename')))
merged_df = merged_df[cols]

# Print the merged DataFrame
print('Result: \n', merged_df)
output_csv_path = os.path.join(args.output_dir, 'merged_result.csv')
merged_df.to_csv(output_csv_path, index=False)
