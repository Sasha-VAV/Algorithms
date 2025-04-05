from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = [0] * (len(nums) - k + 1)
        vals = deque()
        for i, num in enumerate(nums):
            if vals and vals[0] < (i - k + 1):
                vals.popleft()
            while vals and num > nums[vals[-1]]:
                vals.pop()
            vals.append(i)
            if i >= k - 1:
                maximums[i - k + 1] = nums[vals[0]]
        return maximums


if __name__ == '__main__':
    nums = [1, -1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))
