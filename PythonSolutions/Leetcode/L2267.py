class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n = len(grid[0])
        dp = [set()] * n
        dp[0] = {0}
        for row in grid:
            for j, c in enumerate(row):
                x = 1 if c == "(" else -1
                curr = {val + x for val in dp[j] if val + x >= 0}
                
                if j > 0:
                    for val in dp[j - 1]:
                        if val + x >= 0:
                            curr.add(val + x)
                dp[j] = curr
        return 0 in dp[-1]