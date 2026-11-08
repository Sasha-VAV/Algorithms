class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        columns = [0] * m
        rows = [0] * n
        candidates = deque()
        res = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if not x:
                    continue
                rows[i] += 1
                columns[j] += 1
                if rows[i] == 1 and columns[j] == 1:
                    candidates.append((i, j))
                else:
                    res += 1
        while candidates:
            i, j = candidates.popleft()
            if rows[i] == 1 and columns[j] == 1:
                continue
            res += 1
        return res