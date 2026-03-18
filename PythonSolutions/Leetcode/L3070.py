from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        res = 0
        prev_row = [0] * len(grid[0])
        for row in grid:
            curr = 0
            for j, x in enumerate(row):
                prev_row[j] += x
                curr += prev_row[j]
                if curr > k: break
                res += 1
        return res


if __name__ == '__main__':
    arr = [[10], [5]]
    print(Solution().countSubmatrices(arr, 5))