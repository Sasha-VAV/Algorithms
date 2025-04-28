from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        j = 0
        n = len(nums)
        res = 0
        running_sum = 0
        for i, num in enumerate(nums):
            while j < n and (running_sum + nums[j]) * (j - i + 1) < k:
                running_sum += nums[j]
                j += 1
            res += j - i
            running_sum -= num
        return res


if __name__ == '__main__':
    print(Solution().countSubarrays([1, 1, 1], 5))