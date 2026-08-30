class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        min_num = (nums[0], 0)
        max_num = (nums[0], 0)
        n = len(nums)
        for i, num in enumerate(nums):
            if num < min_num[0]:
                min_num = (num, i)
            
            if num > max_num[0]:
                max_num = (num, i)
        
        i, j = min_num[1], max_num[1]
        res = max(i + 1, j + 1)
        res = min(res, max(n - j, n - i))
        res = min(res, i + 1 + n - j)
        res = min(res, n - i + j + 1)
        return res