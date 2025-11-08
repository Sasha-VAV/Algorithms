from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i, j):
            if not grid[i][j] or (i, j) in visited:
                return 0
            visited.add((i, j))
            res = grid[i][j]
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not 0 <= i + a < m or not 0 <= j + b < n: continue
                res += dfs(i + a, j + b)
            return res
        ans = 0
        for x in range(m):
            for y in range(n):
                ans = max(ans, dfs(x, y))
        return ans


if __name__ == '__main__':
    arr = [[8,6],[2,6]]
    print(Solution().findMaxFish(arr))