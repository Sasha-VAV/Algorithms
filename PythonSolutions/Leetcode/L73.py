from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        drop_i = set()
        drop_j = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    drop_i.add(i)
                    drop_j.add(j)
        for i in drop_i:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in drop_j:
                matrix[i][j] = 0


if __name__ == '__main__':
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    Solution().setZeroes(matrix)
    print(matrix)