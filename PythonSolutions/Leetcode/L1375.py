import heapq


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        mins = [0] * n
        min_zero = 0
        res = 0
        for step, idx in enumerate(flips):
            i = idx - 1
            mins[i] = 1
            if i == min_zero:
                if step != n - 1:
                    min_zero = mins.index(0, i+1)
                else:
                    min_zero = n
            if min_zero == step + 1:
                res += 1
        return res