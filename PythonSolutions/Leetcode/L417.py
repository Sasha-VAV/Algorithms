from functools import lru_cache
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        @lru_cache(maxsize=None)
        def go_atlantic(i, j):
            atlantic.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in atlantic and heights[x][y] >= heights[i][j]: go_atlantic(x, y)
        @lru_cache(maxsize=None)
        def go_pacific(i, j):
            pacific.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in pacific and heights[x][y] >= heights[i][j]: go_pacific(x, y)

        for i in range(m):
            if i == 0 or i == m - 1:
                for j in range(n):
                    if i == 0:
                        go_atlantic(i, j)
                    if i == m - 1:
                        go_pacific(i, j)
            go_atlantic(i, 0)
            go_pacific(i, n - 1)
        return sorted([[x, y] for x, y in pacific.intersection(atlantic)])



if __name__ == "__main__":
    arr = [[8,12,0,17,8,7,7,1,12,19,12,19,14,1,16,0,14,7,4,14,14,8,17,18,9,14,19,16,19,17,7,14,13,17,2,11,16,8,8,8]]
    print(Solution().pacificAtlantic(arr))