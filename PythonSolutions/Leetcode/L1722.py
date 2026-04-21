class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], swaps: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x, root_y = self.find(x), self.find(y)
                if root_x == root_y:
                    return
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_y] < self.rank[root_x]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_x] = root_y
                    self.rank[root_x] += 1
        
        n = len(source)
        uf = UnionFind(n)

        for i, j in swaps:
            uf.union(i, j)
        
        ref = defaultdict(lambda: defaultdict(int))
        for i, c in enumerate(source):
            root = uf.find(i)
            ref[root][c] += 1
        
        res = 0
        for i, c in enumerate(target):
            root = uf.find(i)
            if ref[root][c] > 0:
                ref[root][c] -= 1
            else:
                res += 1
        return res