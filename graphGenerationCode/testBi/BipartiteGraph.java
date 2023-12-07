import java.io.*;

public class BipartiteGraph {
    public static void main(String[] args) throws Exception {
        int maxCapacity, minCapacity = 1;
        int n, m = 50;
        double maxProbability = 0.4;

        for (maxCapacity = 1; maxCapacity <= 101; maxCapacity+=10) {
            // int n = 50;  // Number of nodes at end equals number of nodes at start
 
            n = 50;
            m = 50;

            // Construct file name
            String fileName = "bi-" + n + "-" + m + "-" + maxProbability + "-" + minCapacity + "-" + maxCapacity + ".txt";

            // Generate graph and write to file
            generateAndWriteGraph(n, m, maxProbability, minCapacity, maxCapacity, fileName);
        }
    }

    // Method for graph generation and file writing
    private static void generateAndWriteGraph(int n, int m, double maxProbability, int minCapacity, int maxCapacity, String fileName) throws IOException {
        String directory = System.getProperty("user.dir");
        // Append the subdirectory 'bi-m\' to the directory path
        File subDirectory = new File(directory, "bi-c");
        if (!subDirectory.exists()) {
            subDirectory.mkdirs();  // Create the subdirectory if it does not exist
        }

        File file = new File(subDirectory, fileName);
        PrintWriter outFile = new PrintWriter(new FileWriter(file));

        double[][] edge = new double[n][m];
        double value, x;
        System.out.println("\n\n---------------------------------------------------");
        System.out.println("Creating file: " + file.getPath());
        System.out.println("---------------------------------------------------\n");

        // Generating the graph
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                value = Math.random();
                if (value <= maxProbability)
                    edge[i][j] = value;
                else
                    edge[i][j] = 0;
            }
        }

        // Printing and writing the edges
        System.out.println("-----------------------------------------");
        System.out.println("\tSource\tSink\tCapacity");
        System.out.println("-----------------------------------------");

        // Computing the edges out of source
        for (int i = 0; i < n; i++) {
            x = Math.random();
            value = Math.floor(minCapacity + (x * (maxCapacity - minCapacity + 1)));
            System.out.println("\ts" + "\tl" + (i + 1) + "\t" + (int) value);
            outFile.println("s" + "\tl" + (i + 1) + "\t" + (int) value);
        }

        // Computing for the vertices between source and sink
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (edge[i][j] > 0) {
                    edge[i][j] = Math.floor(minCapacity + (edge[i][j] * (maxCapacity - minCapacity + 1)));
                    System.out.println("\tl" + (i + 1) + "\tr" + (j + 1) + "\t" + (int) edge[i][j]);
                    outFile.println("l" + (i + 1) + "\tr" + (j + 1) + "\t" + (int) edge[i][j]);
                }
            }
        }

        // Computing the edges into the sink
        for (int j = 0; j < m; j++) {
            x = Math.random();
            value = Math.floor(minCapacity + (x * (maxCapacity - minCapacity + 1)));
            System.out.println("\tr" + (j + 1) + "\tt" + "\t" + (int) value);
            outFile.println("r" + (j + 1) + "\tt" + "\t" + (int) value);
        }

        System.out.println("\n\nOutput is created at: \t" + directory + "\\" + fileName);
        outFile.close();
    }
}
