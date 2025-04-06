from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while nums[i] != -1:
            x = nums[i]
            nums[i] = -1
            i = x
        return i


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4]
    print(Solution().findDuplicate(nums))
