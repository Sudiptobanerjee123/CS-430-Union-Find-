import sys
import argparse
from union_find_PC import UnionFindWithPathCompression

def main(input_file):
    # Extracting the base name without the extension and appending '_output' with the same extension
    base_name = input_file.split('.')[0]
    output_file = base_name.replace('input', 'output') + '.txt'

    try:
        with open(input_file, 'r') as file:
            n = int(file.readline().strip())  # Number of elements
            m = int(file.readline().strip())  # Number of FIND operations (not directly used)
            find, union = UnionFindWithPathCompression(n)
            results = []

            # Reading the operations
            line = file.readline().strip()
            while line:
                operation = line.split()
                if operation[0] == 'U':
                    union(int(operation[1]) - 1, int(operation[2]) - 1)
                elif operation[0] == 'F':
                    result = find(int(operation[1]) - 1) + 1
                    results.append(result)
                line = file.readline().strip()

        with open(output_file, 'w') as file:
            for result in results:
                file.write(f'{result}\n')
        print(f"Output file generated successfully: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        sys.exit(1)
    except IndexError:
        print("Error: Incorrect operation format in input file.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Union-Find Operations")
    parser.add_argument('-i', '--input', required=True, type=str, help='Input file name')
    args = parser.parse_args()

    main(args.input)
