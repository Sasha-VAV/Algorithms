from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        prev = None
        is_ascent = False
        peaks_left = 2
        if nums[1] <= nums[0]:
            return False
        for num in nums:
            if prev is None:
                prev = num
                continue
            if num > prev and not is_ascent:
                is_ascent = True
                peaks_left -= 1
            if num < prev and is_ascent:
                is_ascent = False
            if num == prev:
                return False
            if peaks_left == -1:
                return False
            prev = num
        return peaks_left == 0 and is_ascent


if __name__ == '__main__':
    arr = [8,9,4,6,1]
    print(Solution().isTrionic(arr))