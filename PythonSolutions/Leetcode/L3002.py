from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        x = len(set1.intersection(set2))
        res = min(len(set1), len(nums1) // 2)
        x -= max(len(set1) - len(nums1) // 2, 0)
        res += min(len(set2), len(nums2) // 2)
        x -= max(len(set2) - len(nums2) // 2, 0)
        return res - max(x, 0)