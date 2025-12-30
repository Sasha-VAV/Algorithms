from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n - 2):
            for j in range(m - 2):
                # distinct
                nums = set()
                for ii in range(3):
                    for jj in range(3):
                        nums.add(grid[i+ii][j+jj])
                if len(nums) != 9:
                    continue
                # between 0 and 9 and int
                if not all(1 <= x <= 9 and int(x) == x for x in nums):
                    continue
                # rows
                row1 = sum(grid[i][j:j+3])
                row2 = sum(grid[i+1][j:j+3])
                row3 = sum(grid[i+2][j:j+3])
                if not (row1 == row2 and row2 == row3):
                    continue
                # cols
                col1 = sum(x[j] for x in grid[i:i+3])
                col2 = sum(x[j+1] for x in grid[i:i+3])
                col3 = sum(x[j+2] for x in grid[i:i+3])
                if not (col1 == col2 and col2 == col3):
                    continue
                #diags
                diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                diag2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]
                if not (diag1 == diag2):
                    continue
                res += 1
        return res


if __name__ == "__main__":
    arr = [[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]
    print(Solution().numMagicSquaresInside(arr))