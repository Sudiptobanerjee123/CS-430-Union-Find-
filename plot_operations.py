import matplotlib.pyplot as plt
import numpy as np
import time
from union_find_PC import UnionFindWithPathCompression


def measure_performance(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            # Read the number of elements
            num_elements = int(file.readline().strip())
            # Read the number of operations
            num_operations = int(file.readline().strip())
            find_op, union_op = UnionFindWithPathCompression(
                num_elements)  # Correctly unpack the tuple here
            start_time = time.time()
            num_unions = 0
            num_finds = 0

            for line in file:
                parts = line.strip().split()
                if parts[0] == 'U':
                    union_op(int(parts[1]) - 1, int(parts[2]) - 1)
                    num_unions += 1
                elif parts[0] == 'F':
                    find_op(int(parts[1]) - 1)
                    num_finds += 1

            end_time = time.time()
            # Calculate the total time taken for all operations
            return num_elements, num_operations, num_unions + num_finds, end_time - start_time
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist.")
        return None


def plot_performance(input_files):
    colors = ['skyblue', 'lightgreen', 'salmon']
    labels = []

    # Adjust figure size for better visualization
    fig, ax = plt.subplots(figsize=(12, 6))

    for idx, file_path in enumerate(input_files):
        result = measure_performance(file_path)
        if result:
            num_elements, num_operations, operations_count, time_taken = result
            label = f'n={num_elements}, m={
                num_operations}, ops={operations_count}'
            labels.append(label)
            ax.bar(idx, time_taken, color=colors[idx], label=label)

    # Set y-axis label and make it bold
    ax.set_ylabel('Time (seconds)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Input Files', fontsize=12,
                  fontweight='bold')  # Added x-axis label
    ax.set_title('Performance of Union-Find with Path Compression for Multiple Inputs',
                 fontsize=14, fontweight='bold')  # Bold title
    ax.set_xticks(np.arange(len(input_files)))
    # Adjust rotation angle and font size for x-axis labels
    ax.set_xticklabels(labels, rotation=0, ha="center", fontsize=10)
    ax.yaxis.grid(True, linestyle='--')  # Adjust y-axis grid style
    ax.legend()
    # Adjust y-axis label font size and make the axis bold
    ax.tick_params(axis='y', labelsize=10, width=2)
    ax.tick_params(axis='x', labelsize=10, width=2)  # Make x-axis labels bold
    plt.tight_layout()  # Ensure proper spacing between subplots
    plt.show()


if __name__ == "__main__":
    # List of input files to analyze
    input_files = ["input.txt", "input1.txt", "input2.txt"]
    plot_performance(input_files)
