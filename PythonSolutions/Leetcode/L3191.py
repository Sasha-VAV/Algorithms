from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                res += 1
                for j in range(3):
                    nums[i + j] = 1 - nums[i + j]
        return res if sum(nums) == len(nums) else -1


if __name__ == '__main__':
    nums = [0,1,1,1,0,0]
    print(Solution().minOperations(nums))