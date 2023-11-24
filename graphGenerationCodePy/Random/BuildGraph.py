import random
import os

def build_graph(file_name, directory, vertices, dense, max_capacity, min_capacity):
    random.seed()  # Initialize random number generator
    graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Building the graph
    for n in range(vertices):
        for m in range(n + 1, vertices):
            random_int = random.randint(min_capacity, max_capacity)
            b = 1 if random.random() < dense / 1000 else 0
            graph[n][m] = graph[m][n] = random_int if b else 0

    # Writing the graph to a file
    dir_name = directory if directory else "."
    output_file_path = os.path.join(dir_name, file_name)

    try:
        with open(output_file_path, 'w') as output:
            for x in range(vertices):
                for y in range(vertices):
                    if graph[x][y] != 0:
                        if x == 0:
                            output.write(f"s {y} {graph[x][y]}\n")
                        elif x == vertices - 1:
                            output.write(f"{y} t {graph[x][y]}\n")
                        else:
                            output.write(f"{x} {y} {graph[x][y]}\n")
        print("\nDone")
    except IOError as e:
        print(f"Error opening file: {e}")

# Example usage
build_graph("graph.txt", ".", 5, 500, 10, 1)
