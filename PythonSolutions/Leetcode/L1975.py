class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        k = 0
        min_val = abs(matrix[0][0])
        res = 0
        for row in matrix:
            for x in row:
                res += abs(x)
                if x < 0:
                    k += 1
                    x = abs(x)
                min_val = min(x, min_val)
        return res - 2 * min_val * (k % 2)