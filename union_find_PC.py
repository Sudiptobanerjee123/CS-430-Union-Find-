def UnionFindWithPathCompression(size):
    parent = list(range(size))
    rank = [0] * size

    def find_root(node):
        if parent[node] != node:
            parent[node] = find_root(parent[node])
        return parent[node]

    def link_roots(rootX, rootY):
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

    def union_rank(x, y):
        rootX, rootY = find_root(x), find_root(y)
        if rootX != rootY:
            link_roots(rootX, rootY)

    return find_root, union_rank
