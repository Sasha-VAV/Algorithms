class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        min_prefix = [0] * (n + 1)
        min_prefix[n] = float('inf')
        for j, x in enumerate(reversed(nums)):
            min_prefix[-j - 2] = min(min_prefix[-j - 1], x)
        
        l = 0
        res = [-1] * n
        while l < n:
            r = l
            current_max = nums[l]
            while r + 1 < n and min_prefix[r + 1] < current_max:
                r += 1
                current_max = max(current_max, nums[r])
            for i in range(l, r + 1):
                res[i] = current_max
            l = r + 1
        return res