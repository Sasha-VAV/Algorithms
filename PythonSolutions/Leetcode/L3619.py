class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        curr = 0
        def dfs(i, j):
            # To minimize recursion footprint
            nonlocal curr
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] == 0:
                return
            curr += grid[i][j]
            grid[i][j] = 0
            for i_shift, j_shift in directions:
                dfs(i + i_shift, j + j_shift)
            return
        res = 0
        for i in range(n):
            for j in range(m):
                curr = 0
                if grid[i][j] == 0:
                    continue
                dfs(i, j)
                if curr > 0 and curr % k == 0:
                    res += 1
        return res