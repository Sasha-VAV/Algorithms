class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] - nums[i] > k:
                res += 1
                i = j
            j += 1
        return res
