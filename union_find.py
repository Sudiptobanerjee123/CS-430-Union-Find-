class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, m):
        if self.parent[m] != m:
            self.parent[m] = self.find(self.parent[m])
        return self.parent[m]

    def union(self, m, n):
        rootM = self.find(m)
        rootN = self.find(n)

        if rootM != rootN:
            if self.rank[rootM] < self.rank[rootN]:
                self.parent[rootM] = rootN
            elif self.rank[rootM] > self.rank[rootN]:
                self.parent[rootN] = rootM
            else:
                self.parent[rootN] = rootM
                self.rank[rootM] += 1
