class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        n = len(nums1)
        m = len(nums2)
        res = 0
        for j in range(m):
            while i < n and i < j and nums1[i] > nums2[j]:
                i += 1
            if i < n and i < j and nums1[i] <= nums2[j]:
                res = max(res, j - i)
        return res
