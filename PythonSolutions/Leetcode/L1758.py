class Solution:
    def minOperations(self, s: str) -> int:
        res = [0, 0]
        for i, prev in enumerate((0, 1)):

            for c in s:
                c = int(c)
                if c == prev:
                    res[i] += 1
                    prev = 1 - c
                else:
                    prev = c
        return min(res)