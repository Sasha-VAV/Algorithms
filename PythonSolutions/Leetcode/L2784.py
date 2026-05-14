class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # For given constraints sorting in the best option
        if len(nums) == 1:
            return False
        nums.sort()
        if nums[-1] != nums[-2]:
            return False
        prev = 0
        for num in islice(nums, len(nums) - 1):
            if num - prev != 1:
                return False
            prev = num
        return True