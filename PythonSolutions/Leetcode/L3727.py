class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(x * x for x in nums)
        min_half = 0
        half = len(nums) // 2
        all_sum = 0
        for i, x in enumerate(nums):
            if i < half:
                min_half += x
            all_sum += x
        return all_sum - 2 * min_half