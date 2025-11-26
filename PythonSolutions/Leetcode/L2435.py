from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        modulo = 1e9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for mod in range(k):
                    if i > 0:
                        dp[i][j][(grid[i][j] + mod) % k] += dp[i-1][j][mod]
                        dp[i][j][(grid[i][j] + mod) % k] %= modulo
                    if j > 0:
                        dp[i][j][(grid[i][j] + mod) % k] += dp[i][j-1][mod]
                        dp[i][j][(grid[i][j] + mod) % k] %= modulo
        return int(dp[-1][-1][0])


if __name__ == '__main__':
    arr = [[5,2,4],[3,0,5],[0,7,2]]
    print(Solution().numberOfPaths(arr, 3))