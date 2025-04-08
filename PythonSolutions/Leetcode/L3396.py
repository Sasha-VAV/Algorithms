import math
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique_numbers = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] in unique_numbers:
                return math.ceil((n - len(unique_numbers)) / 3)
            unique_numbers.add(nums[i])
        return 0


if __name__ == "__main__":
    nums = [1, 2, 1, 1, 1]
    print(Solution().minimumOperations(nums))