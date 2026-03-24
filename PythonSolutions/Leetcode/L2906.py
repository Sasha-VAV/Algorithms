from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        suffix_grid = []
        postfix_grid = []
        suffix_arr = [1] * (n+1)
        postfix_arr = [1] * (n+1)
        mod = 12345
        for i in range(n):
            suffix_grid.append([1] * (m+1))
            postfix_grid.append([1] * (m+1))
            for j in range(m):
                x = grid[i][j]
                y = grid[i][-j-1]
                suffix_grid[i][j+1] = suffix_grid[i][j] * x % mod
                postfix_grid[i][-j-2] = postfix_grid[i][-j-1] * y % mod
        for i in range(n):
            x = suffix_grid[i][-1]
            y = suffix_grid[-i-1][-1]
            suffix_arr[i+1] = suffix_arr[i] * x % mod
            postfix_arr[-i-2] = postfix_arr[-i-1] * y % mod

        res = [[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r = suffix_grid[i][j] * postfix_grid[i][j+1] * suffix_arr[i] * postfix_arr[i+1] % mod
                res[i][j] = r
        return res


if __name__ == "__main__":
    input_grid = [[1], [2]]
    print(Solution().constructProductMatrix(input_grid))