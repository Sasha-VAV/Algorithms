class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x:
                    col_count[j] += 1
                    row_count[i] += 1
        res = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x and col_count[j] == 1 and row_count[i] == 1:
                    res += 1
        return res
