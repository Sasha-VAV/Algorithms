class Solution:
    def findCircleNum(self, connections: List[List[int]]) -> int:
        n = len(connections[0])

        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n
                self.distinct = n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x, root_y = self.find(x), self.find(y)
                if root_x == root_y:
                    return False
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_y] < self.rank[root_x]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_x] = root_y
                    self.rank[root_x] += 1
                self.distinct -= 1
                return True
            
            def get_distinct(self):
                return self.distinct

        dsu = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if connections[i][j]:
                    dsu.union(i, j)
        return dsu.get_distinct()