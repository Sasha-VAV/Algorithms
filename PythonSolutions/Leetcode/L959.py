from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid) * 4 + 1
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == "/":
                    ii = (i + 1) * 4
                    jj = j * 4
                    matrix[ii][jj] = 1
                    matrix[ii-1][jj+1] = 1
                    matrix[ii-2][jj+2] = 1
                    matrix[ii - 3][jj + 3] = 1
                    matrix[ii - 4][jj + 4] = 1
                elif x == "\\":
                    ii = i * 4
                    jj = j * 4
                    matrix[ii][jj] = 1
                    matrix[ii+1][jj+1] = 1
                    matrix[ii+2][jj+2] = 1
                    matrix[ii + 3][jj + 3] = 1
                    matrix[ii + 4][jj + 4] = 1
        def bfs(i, j):
            if not -1 < i < n or not -1 < j < n or matrix[i][j] == 1:
                return False
            matrix[i][j] = 1
            bfs(i + 1, j)
            bfs(i - 1, j)
            bfs(i, j + 1)
            bfs(i, j - 1)
            return True
        res = 0
        for i in range(n):
            for j in range(n):
                if bfs(i, j):
                    res += 1
        return res


if __name__ == '__main__':
    print(Solution().regionsBySlashes(["//","/ "]))