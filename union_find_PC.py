from union_find import UnionFind

class UnionFindWithPathCompression(UnionFind):
    def find(self, k):
        root = k
        while root != self.parent[root]:
            root = self.parent[root]
        
        while k != root:
            next_k = self.parent[k]
            self.parent[k] = root
            k = next_k
        
        return root
