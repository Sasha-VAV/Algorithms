from collections import deque
from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l = 0
        r = len(cells) - 1
        res = -1
        ref = [[-1] * col for _ in range(row)]
        for i, (x, y) in enumerate(cells):
            ref[x-1][y-1] = i

        def possible(day):
            q = deque()
            for j in range(col):
                if ref[0][j] > day:
                    q.appendleft((j, 0))
            visited = set()
            while q:
                x, y = q.pop()
                if not (0 <= y < row and 0 <= x < col):
                    continue
                if ref[y][x] <= day:
                    continue
                if (x, y) in visited:
                    continue
                if y == row - 1:
                    return True
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    q.appendleft((x + dx, y + dy))

        while l <= r:
            m = l + (r - l + 1) // 2
            if possible(m):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res + 1


if __name__ == '__main__':
    row = 3
    col = 3
    cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
    print(Solution().latestDayToCross(row, col, cells))
