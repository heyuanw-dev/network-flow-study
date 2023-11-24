import random
import sys

def graph_builder(v, e, min_capacity, max_capacity):
    bfr = []
    
    # Add distinguished node s
    for _ in range(e):
        while True:
            head = random.randint(1, v)
            if head not in bfr:
                bfr.append(('s', f'v{head}', random.randint(min_capacity, max_capacity)))
                break

    # Add distinguished node t
    for _ in range(e):
        while True:
            tail = random.randint(1, v)
            if tail not in bfr:
                bfr.append((f'v{tail}', 't', random.randint(min_capacity, max_capacity)))
                break

    # Add internal nodes
    for i in range(1, v + 1):
        s = set([i])
        for _ in range(e):
            while True:
                head = random.randint(1, v)
                if head not in s:
                    s.add(head)
                    bfr.append((f'v{i}', f'v{head}', random.randint(min_capacity, max_capacity)))
                    break

    return bfr

def to_file(graph, filename):
    with open(filename, 'w') as file:
        for tail, head, capacity in graph:
            file.write(f'{tail} {head} {capacity}\n')

def main():
    if len(sys.argv) != 6:
        print("\nInvalid parameters!")
        print("Usage: python random_graph.py v e min max f")
        print("[... Usage instructions ...]")
        return

    v, e, min_capacity, max_capacity, filename = map(int, sys.argv[1:5]) + [sys.argv[5]]

    if v > e and max_capacity >= min_capacity:
        graph = graph_builder(v, e, min_capacity, max_capacity)
        to_file(graph, filename)
        print("\nDONE!")
    else:
        print("\nFAIL!")
        if v <= e:
            print("The number of vertices must exceed the number of edges leaving each node.")
        else:
            print("Max must be greater than or equal to min.")

if __name__ == "__main__":
    main()
