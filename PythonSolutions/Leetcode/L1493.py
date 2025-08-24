class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = None
        curr = 0
        res = 0
        for num in nums:
            if num == 0:
                if prev is None: prev = 0
                res = max(res, prev + curr)
                prev = curr
                curr = 0
            else:
                curr += 1
        if prev is None: return curr - 1
        return max(res, prev + curr)