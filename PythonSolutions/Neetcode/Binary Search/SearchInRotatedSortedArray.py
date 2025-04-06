from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[right]:
                if target > nums[mid] >= nums[left] or nums[right] >= target > nums[mid] or nums[mid] >= nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    print(Solution().search(nums, target))
