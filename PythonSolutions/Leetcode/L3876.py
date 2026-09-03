class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_number = nums1[0]
        has_odd = False

        for num in nums1:
            if num < min_number:
                min_number = num
            if num & 1:
                has_odd = True

        if min_number & 1:
            return True
        return not has_odd 