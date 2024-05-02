import matplotlib.pyplot as plt
import numpy as np
import time
from union_find_PC import UnionFindWithPathCompression

def measure_performance_from_file(input_file):
    with open(input_file, 'r') as file:
        n = int(file.readline().strip()) 
        m = int(file.readline().strip())
        uf = UnionFindWithPathCompression(n)
        start_time = time.time()
        num_unions = 0
        num_finds = 0

        for line in file:
            parts = line.strip().split()
            if parts[0] == 'U':
                uf.union(int(parts[1]) - 1, int(parts[2]) - 1)
                num_unions += 1
            elif parts[0] == 'F':
                uf.find(int(parts[1]) - 1)
                num_finds += 1

        end_time = time.time()
        return n, m, num_unions + num_finds, end_time - start_time

def plot_performance(input_file):
    n, m, operations_count, time_taken = measure_performance_from_file(input_file)
    
    plt.bar(['Operations'], [time_taken], label=f'n={n}, m={m}, ops={operations_count}')
    plt.xlabel('Test Scenario')
    plt.ylabel('Time (seconds)')
    plt.title('Performance of Union-Find with Path Compression for Given Input')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    input_file = "input.txt"
    plot_performance(input_file)
