class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = []
        for i in range(m):
            row = [0] * n
            r = rowSum[i]
            for j in range(n):
                c = colSum[j]
                if c < r:
                    r -= c
                    row[j] = c
                    colSum[j] = 0
                else:
                    row[j] = r
                    colSum[j] -= r
                    break
            res.append(row)
        return res