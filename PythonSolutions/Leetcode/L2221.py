from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]
        arr = nums[:-1]
        while len(arr) > 0:
            for i, x in enumerate(nums[1:]):
                arr[i] += x
                arr[i] %= 10
            nums = arr
            arr = arr[:-1]
        return nums[0]


if __name__ == '__main__':
    print(Solution().triangularSum([1,2,3,4,5]))