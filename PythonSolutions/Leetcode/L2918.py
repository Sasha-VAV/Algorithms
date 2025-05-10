from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.count(0)
        b = nums2.count(0)
        c = sum(nums1)
        d = sum(nums2)
        if a == 0 and c < (b+d):
            return -1
        if b == 0 and d < (a+c):
            return -1
        return max(a+c, b+d)

