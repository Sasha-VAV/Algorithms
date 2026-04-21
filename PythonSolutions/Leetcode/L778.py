class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
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
                    return
                if self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                elif self.rank[root_y] < self.rank[root_x]:
                    self.parent[root_y] = root_x
                else:
                    self.parent[root_x] = root_y
                    self.rank[root_x] += 1
                self.distinct -= 1

            def is_requirement_satisfied(self):
                return self.find(0) == self.find(len(self.parent) - 1)

        heap = []
        n = len(grid)
        if n == 1:
            return grid[0][0]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                heapq.heappush(heap, (x, i, j))
        uf = UnionFind(n ** 2)
        shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            price, i, j = heapq.heappop(heap)
            pos1 = n * i + j
            for i_shift, j_shift in shifts:
                i_shift, j_shift = i + i_shift, j + j_shift
                if not (0 <= i_shift < n and 0 <= j_shift < n) or grid[i_shift][j_shift] > price:
                    continue
                pos2 = n * i_shift + j_shift
                uf.union(pos1, pos2)
                if uf.is_requirement_satisfied():
                    return price
        raise NotImplementedError