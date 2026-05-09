from typing import List
from collections import deque


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        max_depth = min(m, n) // 2
        for d in range(max_depth):
            i1, j1 = d, d
            i2, j2 = n - d - 1, m - d - 1
            q = deque()
            direction = "down"
            i, j = i1, j1
            curr_k = k % ((i2 - i1 + j2 - j1) * 2)
            if curr_k == 0:
                continue
            made_loop = False
            while not made_loop or q:
                if not made_loop:
                    q.appendleft(grid[i][j])
                if made_loop or len(q) > curr_k:
                    grid[i][j] = q.pop()
                
                while True:
                    if direction == "down":
                        if i == i2:
                            direction = "right"
                        else:
                            i += 1
                            break
                    if direction == "right":
                        if j == j2:
                            direction = "up"
                        else:
                            j += 1
                            break
                    if direction == "up":
                        if i == i1:
                            direction = "left"
                        else:
                            i -= 1
                            break
                    if direction == "left":
                        if j == j1:
                            direction = "down"
                            made_loop = True
                            q.popleft()
                        else:
                            j -= 1
                            break
        return grid


if __name__ == "__main__":
    grid = [[40,10],[30,20]]
    k = 2
    print(Solution().rotateGrid(grid, k))