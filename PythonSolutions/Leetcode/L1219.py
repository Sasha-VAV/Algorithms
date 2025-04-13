from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_amount = 0
        m = len(grid)
        n = len(grid[0])
        def cell_max(i, j):
            if grid[i][j] == 0:
                return 0
            x = grid[i][j]
            grid[i][j] = 0
            tmp = 0
            if i > 0:
                tmp = max(tmp, cell_max(i-1,j))
            if j > 0:
                tmp = max(tmp, cell_max(i,j-1))
            if i < m - 1:
                tmp = max(tmp, cell_max(i+1,j))
            if j < n - 1:
                tmp = max(tmp, cell_max(i,j+1))
            grid[i][j] = x
            return x + tmp
        for i in range(m):
            for j in range(n):
                max_amount = max(cell_max(i,j), max_amount)
        return max_amount