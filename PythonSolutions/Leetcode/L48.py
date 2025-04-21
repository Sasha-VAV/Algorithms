from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            row = []
            for j in range(n):
                if j + i < n:
                    row.insert(0, matrix[i+j][i])
                else:
                    row.append(matrix[i][-j-1])
            prev = matrix[i]
            matrix[i] = row
            for j in range(i + 1, n):
                matrix[j][i] = prev[j]
        pass


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().rotate(matrix))
    print(matrix)