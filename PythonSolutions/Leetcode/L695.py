class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def bfs(i, j):
            if not -1 < i < m or not -1 < j < n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = bfs(i, j-1)
            area += bfs(i, j+1)
            area += bfs(i-1, j)
            area += bfs(i+1, j)
            return area + 1
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, bfs(i, j))
        return res