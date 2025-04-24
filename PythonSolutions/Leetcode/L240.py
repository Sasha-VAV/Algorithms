from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def bfs(i, j):
            if not -1 < i < m or not -1 < j < n:
                return False
            x = matrix[i][j]
            if x > target:
                return False
            if x == target:
                return True
            matrix[i][j] = target + 1
            return bfs(i+1, j) or bfs(i, j+1) or bfs(i-1, j) or bfs(i, j-1)
        return bfs(0, 0)