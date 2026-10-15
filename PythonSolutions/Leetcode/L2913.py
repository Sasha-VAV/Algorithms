class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            counts = [0] * 101
            n_distinct = 0
            for j in range(i, len(nums)):
                counts[nums[j]] += 1    
                if counts[nums[j]] == 1:
                    n_distinct += 1
                res += n_distinct * n_distinct
        return res