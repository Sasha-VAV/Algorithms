from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 0
        curr_len = 0
        for i, num in enumerate(nums):
            if i == 0 or num > nums[i - 1]:
                curr_len += 1
            else:
                max_len = max(curr_len, max_len)
                curr_len = 1
        max_len = max(curr_len, max_len)
        return max_len
