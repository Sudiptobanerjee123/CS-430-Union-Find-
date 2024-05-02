def UnionFindWithPathCompression(size):
    try:
        # Initialize parent and rank arrays
        parent = list(range(size))  # Each element initially points to itself
        rank = [0] * size  # Initialize ranks of all elements to 0

        # Function to find the root of a set with path compression
        def find_root(node):
            if parent[node] != node:  # If the node is not the root
                parent[node] = find_root(parent[node])  # Recursively find and update parent until reaching the root
            return parent[node]  # Return the root

        # Function to link roots of two sets based on their ranks
        def link_roots(rootX, rootY):
            if rank[rootX] < rank[rootY]:  # Attach smaller tree to the root of the larger tree
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:  # If ranks are equal, arbitrarily choose one as the parent and increment its rank
                parent[rootY] = rootX
                rank[rootX] += 1

        # Function to perform union operation based on ranks
        def union_rank(x, y):
            # Find the roots of the sets containing x and y
            rootX, rootY = find_root(x), find_root(y)
            if rootX != rootY:  # If they are not already in the same set
                link_roots(rootX, rootY)  # Merge the sets by linking their roots

        return find_root, union_rank

    except Exception as e:
        print(f"An error occurred during UnionFindWithPathCompression initialization: {e}")
