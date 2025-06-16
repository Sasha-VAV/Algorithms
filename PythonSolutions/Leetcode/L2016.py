class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        min_x = float('inf')
        max_x = -1
        for x in nums:
            if x < min_x:
                min_x = x
                max_x = -1
            elif x > max_x and x > min_x:
                max_x = x
            if min_x != float('inf') and max_x != -1:
                res = max(res, max_x - min_x)
        return res