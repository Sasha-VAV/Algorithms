class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        total = m * n

        k %= total
        q = deque()

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                i_relative = j + i * m
                q.appendleft(x)
                if len(q) <= k:
                    i_relative -= k
                    i_relative %= total

                    grid[i][j] = grid[i_relative // m][i_relative % m]
                else:
                    grid[i][j] = q.pop()

        return grid