from collections import defaultdict


class Solution:
    def find_horizontal_cut(self, grid: list[list[int]], total: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        curr = 0
        unique_values = defaultdict(list)
        if n < 2:
            return False
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                unique_values[x].append((i, j))
                curr += x
            diff = 2 * curr - total
            if diff < 0:
                continue
            if diff == 0:
                return True
            for x, y in unique_values[diff]:
                if i == 0 and 0 < y < m - 1: continue
                if m == 1 and 0 < x < i: continue
                return True
        return False

    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        total_sum = sum(sum(row) for row in grid)
        for _ in range(4):
            if self.find_horizontal_cut(grid, total_sum): return True
            grid = list(zip(*grid[::-1]))
        return False


if __name__ == '__main__':
    arr = [[10,5,4,5]]
    print(Solution().canPartitionGrid(arr))
