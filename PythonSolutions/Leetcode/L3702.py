class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = 0
        any_non_zero = False
        for num in nums:
            any_non_zero = any_non_zero or num
            res ^= num
        if res > 0:
            return len(nums)
        if any_non_zero:
            return len(nums) - 1
        return 0
        