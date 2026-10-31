MODULO = 10 ** 9 + 7

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [0] * m
        mirror_bank = defaultdict(int) # i j incoming dir 0 - left 1 - up
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i == 0 and j == 0:
                    dp[0] = 1
                    continue
                    
                if x == 1:
                    mirror_bank[(i, j + 1, 1)] += dp[j] + mirror_bank[(i, j, 0)]
                    if j > 0:
                        mirror_bank[(i + 1, j, 0)] = dp[j - 1] + mirror_bank[(i, j, 1)]
                    dp[j] = 0
                    continue
                
                curr = mirror_bank[(i, j, 0)] + mirror_bank[(i, j, 1)]
                mirror_bank.pop((i, j, 0))
                mirror_bank.pop((i, j, 1))
                if j > 0:
                    curr += dp[j - 1]
                curr += dp[j]
                dp[j] = curr % MODULO
        return dp[-1]