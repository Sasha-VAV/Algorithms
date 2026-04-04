from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 1
        max_achieved = 1
        while j < len(nums):
            if nums[j] <= nums[i] * k:
                max_achieved = max(max_achieved, j - i + 1)
                j += 1
            else:
                i += 1
        return len(nums) - max_achieved


if __name__ == '__main__':
    arr = [8,99,65,16,39]
    print(Solution().minRemoval(arr, 3))