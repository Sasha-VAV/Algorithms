from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        operations = []
        val = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tmp = grid[i][j] - val
                if tmp % x != 0:
                    return -1
                operations.append(tmp // x)
        operations.sort()
        tmp = operations[0]
        for i in range(len(operations)):
            operations[i] -= tmp
        left = 0
        right = sum(operations)
        n = len(operations)
        min_ops = left + right
        for i in range(1, n):
            tmp = operations[i]
            diff = tmp - operations[i - 1]
            left += i * diff
            right -= (n - i) * diff
            min_ops = min(min_ops, left + right)

        return min_ops

if __name__ == "__main__":
    grid = [[529,529,989],[989,529,345],[989,805,69]]
    x = 92
    print(Solution().minOperations(grid, x))