class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])
        for i, row in enumerate(mat):
            if i % 2 == 0:
                curr_row = row[-k:] + row[:-k]
            else:
                curr_row = row[k:] + row[:k]
            if curr_row != row: return False
        return True
