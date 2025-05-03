from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = []
        matrix = []
        for i in range(n):
            matrix.append([-1]*n)
        dp.append(matrix)
        dp[0][0][n-1] = grid[0][0] + grid[0][n-1]
        for i in range(1,m):
            matrix = []
            for j in range(n):
                row = []
                for k in range(n):
                    x = dp[i-1][j][k]
                    if k > 0: x = max(x, dp[i-1][j][k-1])
                    if j > 0: x = max(x, dp[i-1][j-1][k])
                    if j < n - 1: x = max(x, dp[i-1][j+1][k])
                    if k < n - 1: x = max(x, dp[i-1][j][k+1])
                    if j > 0 and k > 0: x = max(x, dp[i-1][j-1][k-1])
                    if j > 0 and k < n - 1: x = max(x, dp[i-1][j-1][k+1])
                    if j < n - 1 and k > 0: x = max(x, dp[i-1][j+1][k-1])
                    if j < n - 1 and k < n - 1: x = max(x, dp[i-1][j+1][k+1])
                    if x > -1:
                        if j == k:
                            row.append(x + grid[i][j])
                        else:
                            row.append(x + grid[i][j] + grid[i][k])
                    else:
                        row.append(-1)
                matrix.append(row)
            dp.append(matrix)
        res = -1
        for row in dp[-1]:
            res = max(res, max(row))
        return res


if __name__ == '__main__':
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(Solution().cherryPickup(grid))