import sys
from union_find_PC import UnionFindWithPathCompression

def main(input_file, output_file):
    print("Reading input file...")
    with open(input_file, 'r') as file:
        n = int(file.readline().strip())
        uf = UnionFindWithPathCompression(n)
        results = []

        print("Processing operations...")
        for line in file:
            parts = line.strip().split()
            if parts[0] == 'U':
                uf.union(int(parts[1]) - 1, int(parts[2]) - 1)
            elif parts[0] == 'F':
                result = uf.find(int(parts[1]) - 1) + 1
                results.append(result)

    print("Writing output file...")
    with open(output_file, 'w') as file:
        for result in results:
            file.write(f'{result}\n')

    print("Output file generated successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <inputfile> <outputfile>")
        sys.exit(1)

    print("Starting the program...")
    main(sys.argv[1], sys.argv[2])
