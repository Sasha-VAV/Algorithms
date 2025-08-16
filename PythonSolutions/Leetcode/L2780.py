from typing import List
from collections import Counter


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        most_common, val = Counter(nums).most_common()[0]
        a = 0
        b = 0
        for i, num in enumerate(nums):
            if num == most_common:
                a += 1
            else:
                b += 1
            if a > b:
                rest = len(nums) - i - 1
                if 2 * (val - a) > rest: return i
        return -1


if __name__ == '__main__':
    nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
    print(Solution().minimumIndex(nums))