class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = 0
        curr = nums[0]
        for x, y in zip(nums[:-1], nums[1:]):
            if x < y:
                curr += y
            else:
                res = max(res, curr)
                curr = y
        return max(res, curr)