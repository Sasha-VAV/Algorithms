from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while right - left > 2:
            mid = (right + left) // 2
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
        return min(nums[left:left + 3])


if __name__ == '__main__':
    nums=[3,4,5,6,1,2]
    print(Solution().findMin(nums))
