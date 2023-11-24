import random
import sys

class MeshGenerator:
    def __init__(self, args):
        # Default values
        self.m = 3  # number of rows
        self.n = 4  # number of columns
        self.c = 1  # capacity
        self.constCap = False
        self.out = sys.stdout

        # Parse command line arguments
        if len(args) >= 2:
            self.m = int(args[0])
            self.n = int(args[1])

        if len(args) >= 3:
            self.c = int(args[2])

        if len(args) == 5 and args[4] == "-cc":
            self.constCap = True

        if len(args) >= 4 and args[3] != "-cc":
            try:
                self.out = open(args[3], 'w')
            except FileNotFoundError:
                print(f"Exception thrown on file formation: {args[3]}")
                sys.exit(1)

        if len(args) == 4 and args[3] == "-cc":
            self.constCap = True

    def capacity(self):
        if self.constCap:
            return self.c
        return random.randint(1, self.c)

    def line(self, i1, j1, i2, j2, cap):
        self.out.write(f"({i1},{j1}) ({i2},{j2}) {cap}\n")

    def generate(self):
        for i in range(1, self.m + 1):
            self.line('s', '', i, 1, self.capacity())

        for j in range(1, self.n):
            for i in range(1, self.m + 1):
                self.line(i, j, i, j + 1, self.capacity())

        for j in range(1, self.n + 1):
            for i in range(1, self.m):
                self.line(i, j, i + 1, j, self.capacity())
                self.line(i + 1, j, i, j, self.capacity())

        for i in range(1, self.m + 1):
            self.line(i, self.n, 't', '', self.capacity())

        if isinstance(self.out, file):
            self.out.close()

def main(args):
    mesh = MeshGenerator(args)
    mesh.generate()

if __name__ == "__main__":
    main(sys.argv[1:])
