from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = nums[0]
        m = nums[1]
        res = 0
        for r in nums[2:]:
            if (l+r)*2 == m: res += 1
            m, l = r, m
        return res