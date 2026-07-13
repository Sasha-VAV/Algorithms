class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.rank = [0] * n
        self.sizes = {k: 1 for k in range(n)}
        # Since no repeated edges
        self.edges = {k: 0 for k in range(n)}

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        self.edges[root_a] += 1

        if root_a == root_b:
            return

        rank_a = self.rank[a]
        rank_b = self.rank[b]

        if rank_a < rank_b:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
            self.edges[root_b] += self.edges[root_a]
            self.sizes.pop(root_a)
            self.edges.pop(root_a)
        elif rank_a > rank_b:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
            self.edges[root_a] += self.edges[root_b]
            self.sizes.pop(root_b)
            self.edges.pop(root_b)
        else:
            self.parents[root_a] = root_b
            self.rank[root_a] += 1
            self.sizes[root_b] += self.sizes[root_a]
            self.edges[root_b] += self.edges[root_a]
            self.sizes.pop(root_a)
            self.edges.pop(root_a)

    def get_full_connected(self):
        res = 0
        for k, v in self.sizes.items():
            if self.edges[k] == v * (v - 1) // 2:
                res += 1
        return res


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.connect(x, y)

        return uf.get_full_connected()
