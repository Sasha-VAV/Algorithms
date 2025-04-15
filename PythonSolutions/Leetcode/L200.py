from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def bfs(r, c):
            nonlocal visited
            q = deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                visited.add((r,c))
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for h, w in directions:
                    nr, nc = r + h, c + w
                    if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited or grid[nr][nc] == '0':
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))