# Introduction To Algorithms CS-430 (Project)

## Contributors

- **Name:** Sudipta Banerjee
- **CWID:** A20460632
- **Email:** sbanerjee5@hawk.iit.edu

## Union-Find and Union-Find with Path Compression (Description)

This project implements two algorithms: Union-Find and Union-Find with Path Compression. These data structures are used to maintain disjoint sets and perform operations such as finding the representative element of a set and merging (unioning) two sets.

## Algorithm Descriptions

### 1. Union-Find

The Union-Find data structure is used to maintain a collection of disjoint (non-overlapping) sets. It supports two main operations:

- **Union(x, y)**: Merge the sets containing elements `x` and `y` into a single set.
- **Find(x)**: Determine the representative element (root) of the set that contains `x`.

This implementation uses the **Union by Rank** heuristic, which aims to keep the tree as flat as possible by attaching the smaller tree (by rank) to the root of the larger tree during a union operation. The rank of a node is an upper bound on the height of the node in the tree.

#### Implementation Details

- The `UnionFind` class is implemented in the `union_find.py` file.
- The `__init__` method initializes the data structure with `size` elements, where each element is initially its own root with rank 0.
- The `find` method follows the parent pointers until it reaches the root of the set containing the given element.
- The `union` method first finds the roots of the sets containing `x` and `y` using the `find` method. If the roots are different, it merges the sets by attaching the smaller ranked tree to the root of the larger ranked tree. If the ranks are equal, it arbitrarily chooses one root as the parent and increments its rank.

### 2. Union-Find with Path Compression

The Union-Find with Path Compression algorithm is an optimization of the basic Union-Find algorithm. It includes path compression, which flattens the tree during the `find` operation by directly linking each visited node to the root of the set.

#### Implementation Details

- The `UnionFindWithPathCompression` class is implemented in the `union_find_PC.py` file and inherits from the `UnionFind` class.
- The `find` method is overridden to include path compression. It first finds the root of the set using the standard `find` algorithm. Then, while traversing back up the path, it directly links each visited node to the root, effectively flattening the tree.
- The `union` method is inherited from the `UnionFind` class and performs the union operation using the Union by Rank heuristic.

## Main function

The project includes a `main.py` file that serves as the entry point for executing the algorithms. It reads input from a file, processes the operations, and writes the output to another file.

## Run the Program

To run the program, use the following command:

```bash
python3 main.py -i <inputfile>
```

### Replace input_file with input.txt and output_file with output.txt

```bash
python3 main.py -i input.txt
```
