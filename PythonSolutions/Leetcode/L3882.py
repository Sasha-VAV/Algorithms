class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [set() for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                new_set = set()
                if i == 0 and j == 0:
                    new_set.add(x)
                if i > 0:
                    for v in dp[j]:
                        new_set.add(x ^ v)
                if j > 0:
                    for v in dp[j - 1]:
                        new_set.add(x ^ v)
                dp[j] = new_set
        return min(dp[-1])