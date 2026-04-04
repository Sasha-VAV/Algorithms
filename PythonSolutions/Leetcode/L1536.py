class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zeros = []
        n = len(grid)
        for row in grid:
            for i, x in enumerate(reversed(row)):
                if x == 1:
                    zeros.append(i)
                    break
            else:
                zeros.append(n)
        res = 0
        for i, x in enumerate(sorted(zeros)):
            if x < i: return -1

        for i in range(n):
            needed = n - i - 1
            j = i
            while zeros[j] < needed:
                j += 1
            if j == n: return -1
            while i < j:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                j -= 1
                res += 1
        return res