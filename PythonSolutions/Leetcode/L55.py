class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        j = nums[0]
        for i, num in enumerate(nums):
            if i > j:
                return False
            j = max(i+num, j)
        return True