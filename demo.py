# Purpose for demoing for TCSS 543 final project.

import subprocess
import pandas as pd
import os
import platform
import psutil

# Function to run a script in its directory
def run_script(script_path):
    # Save the current directory
    original_dir = os.getcwd()

    # Change to the script's directory
    os.chdir(os.path.dirname(script_path))

    # Run the script
    subprocess.run(["python", os.path.basename(script_path)], check=True)

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

# Paths to the Python scripts
script_paths = [
    "fordFulkerson/runFordFulkerson.py",
    "scalingFF/runScalingFF.py",
    "preflowPush/runPP.py"
]

# Execute each script
for script in script_paths:
    print('running: ' , script)
    run_script(script)
    print('Complete executing: ', script)

# Paths to the CSV files, need to change if you altereed the dataset output in run(algo).py
csv_paths = [
    "csvs/ff-bipartite-t.csv",
    "csvs/preflowdf-t.csv",
    "csvs/scaling-t.csv"
]

# Read and merge the CSV files. This is for displaying three algorithms' result in terminal. you can use merged_df.to_csv to output the dataset.
dfs = [pd.read_csv(csv) for csv in csv_paths]
merged_df = pd.concat(dfs, axis=1, join='inner')
merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^Unnamed')]


# Print the merged DataFrame
print('Result: \n', merged_df)
