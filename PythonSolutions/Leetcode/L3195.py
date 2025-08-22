from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        fa = fb = sa = sb = None
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if not x: continue
                if fa is None: fa = i
                if fb is None: fb = j
                if sa is None: sa = i
                if sb is None: sb = j
                fa = min(fa, i)
                fb = min(fb, j)
                sa = max(sa, i)
                sb = max(sb, j)

        return (sa - fa + 1) * (sb - fb + 1)


if __name__ == '__main__':
    grid = [[0,1,0],[1,0,1]]
    print(Solution().minimumArea(grid))