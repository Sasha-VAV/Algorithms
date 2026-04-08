class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [float('inf')] * m
        dp[0] = 0
        for row in grid:
            for j, x in enumerate(row):
                curr = dp[j]
                if j > 0:
                    curr = min(curr, dp[j-1])
                dp[j] = curr + x
        return dp[-1]