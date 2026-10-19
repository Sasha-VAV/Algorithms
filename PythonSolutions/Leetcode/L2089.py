class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        prefix = 0
        suffix = 0
        for num in nums:
            if num < target:
                prefix += 1
            elif num > target:
                suffix += 1
        return list(range(prefix, len(nums) - suffix))