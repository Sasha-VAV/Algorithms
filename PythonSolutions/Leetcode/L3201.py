class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = [0] * 4
        prev = [True, False]
        for i, x in enumerate(nums):
            if x % 2 == 0:
                res[0] += 1
            else:
                res[1] += 1
            if (x % 2 == 0) ^ prev[0]:
                res[2] += 1
                prev[0] = not prev[0]
            if (x % 2 == 0) ^ prev[1]:
                res[3] += 1
                prev[1] = not prev[1]
        return max(res)