from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        for i, num in enumerate(nums):
            if numbers.get(target - num, -1) + 1:
                ans = [numbers.get(target - num), i]
                return ans
            numbers[num] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
