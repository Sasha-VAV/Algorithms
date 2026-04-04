from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        res = []
        for i in range(n-k+1):
            res.append([])
            for j in range(m-k+1):
                curr = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        curr.append(grid[x][y])
                curr.sort()
                prev = None
                value = float('inf')
                for x in curr:
                    if not prev is None and x != prev:
                        value = min(value, x - prev)
                    prev = x
                if value == float('inf'):
                    value = 0
                res[-1].append(value)
        return res


if __name__ == '__main__':
    arr = [[1,8],[3,-2]]
    print(Solution().minAbsDiff(arr, 2))