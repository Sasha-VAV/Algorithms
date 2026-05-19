class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        len1 = len(nums1)
        len2 = len(nums2)
        while left < len1 and right < len2:
            if nums1[left] == nums2[right]:
                return nums1[left]
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                left += 1
        return -1