class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i, num in enumerate(nums):
            if num == i:
                continue
            res &= num
        return 0 if res == -1 else res