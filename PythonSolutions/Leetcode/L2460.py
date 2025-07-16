class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        j = 0
        for i in range(len(nums) - 1):
            if nums[i] != 0:
                if nums[i] == nums[i + 1]:
                    nums[i + 1] = 0
                    nums[i] *= 2
                res[j] = nums[i]
                j += 1
        if nums[-1] != 0:
            res[j] = nums[-1]
            j += 1
        return res
