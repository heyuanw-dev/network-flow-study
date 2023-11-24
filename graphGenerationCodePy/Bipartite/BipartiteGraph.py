import os
import random

def get_string():
    return input()

def get_int():
    return int(input())

def get_real():
    return float(input())

def main():
    print("\n\n---------------------------------------------------")
    n = int(input("Enter number of nodes on the source side: \t"))
    m = int(input("Enter number of nodes on the sink side: \t"))
    max_probability = float(input("Enter max probability: \t\t\t\t"))
    if max_probability > 1:
        print("Max probability should be less than or equal to 1")
        return
    min_capacity = int(input("Enter minimum capacity: \t\t\t"))
    max_capacity = int(input("Enter maximum capacity: \t\t\t"))
    directory = os.getcwd()
    file_name = input("Enter the output file name: \t\t\t") + ".txt"
    print("---------------------------------------------------\n")

    try:
        with open(os.path.join(directory, file_name), 'w') as outfile:
            edge = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    value = random.random()
                    if value <= max_probability:
                        edge[i][j] = value
                    else:
                        edge[i][j] = 0

            print("-----------------------------------------")
            print("\tSource\tSink\tCapacity")
            print("-----------------------------------------") 

            for i in range(n):
                value = min_capacity + int(random.random() * (max_capacity - min_capacity + 1))
                print("\ts\tl" + str(i + 1) + "\t" + str(value))
                outfile.write("\ts\tl" + str(i + 1) + "\t" + str(value) + "\n")

            for i in range(n):
                for j in range(m):
                    if edge[i][j] > 0:
                        edge[i][j] = min_capacity + int(edge[i][j] * (max_capacity - min_capacity + 1))
                        print("\tl" + str(i+1) + "\tr" + str(j+1) + "\t" + str(int(edge[i][j])))
                        outfile.write("\tl" + str(i+1) + "\tr" + str(j+1) + "\t" + str(int(edge[i][j])) + "\n")

            for j in range(m):
                value = min_capacity + int(random.random() * (max_capacity - min_capacity + 1))
                print("\tr" + str(j+1) + "\tt\t" + str(value))
                outfile.write("\tr" + str(j + 1) + "\tt\t" + str(value) + "\n")

            print("\n\nOutput is created at: \t" + os.path.join(directory, file_name))

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
