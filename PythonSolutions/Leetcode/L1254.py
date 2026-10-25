class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        def dfs(i, j):
            nonlocal grid
            if i < 0 or i >= n or j < 0 or j >= m:
                return -1
            if 1 <= grid[i][j] <= 2:
                return grid[i][j]
            is_island = True
            grid[i][j] = 2
            for i_shift, j_shift in directions:
                if dfs(i + i_shift, j + j_shift) == -1:
                    is_island = False
            if is_island:
                return 2
            return -1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                if dfs(i, j) != -1:
                    res += 1
        return res