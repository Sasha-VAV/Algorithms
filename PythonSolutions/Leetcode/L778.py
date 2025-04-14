from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        l = 0
        r = 2500
        n = len(grid)
        for arr in grid:
            for x in arr:
                r = max(r, x)
        def is_enough(t, i, j):
            res = grid[i][j]
            if i == n-1 and j == n-1:
                return True
            if res == -1 or res > t:
                return False
            grid[i][j] = -1
            ok = False
            if i > 0 and grid[i-1][j] <= t:
                ok = ok or is_enough(t, i-1, j)
            if j > 0 and grid[i][j-1] <= t:
                ok = ok or is_enough(t, i, j-1)
            if j < n-1 and grid[i][j+1] <= t:
                ok = ok or is_enough(t, i, j+1)
            if i < n-1 and grid[i+1][j] <= t:
                ok = ok or is_enough(t, i+1, j)
            grid[i][j] = res
            return ok
        best = r
        while l <= r:
            mid = (l+r)//2
            if is_enough(mid, 0, 0):
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best


if __name__ == '__main__':
    grid = [[26,99,80,1,89,86,54,90,47,87],[9,59,61,49,14,55,77,3,83,79],[42,22,15,5,95,38,74,12,92,71],[58,40,64,62,24,85,30,6,96,52],[10,70,57,19,44,27,98,16,25,65],[13,0,76,32,29,45,28,69,53,41],[18,8,21,67,46,36,56,50,51,72],[39,78,48,63,68,91,34,4,11,31],[97,23,60,17,66,37,43,33,84,35],[75,88,82,20,7,73,2,94,93,81]]
    print(Solution().swimInWater(grid))