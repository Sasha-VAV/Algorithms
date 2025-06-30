from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for k, v in counter.items():
            if k - 1 in counter:
                res = max(res, counter[k - 1] + v)
        return res


if __name__ == '__main__':
    nums = [1,3,2,2,5,2,3,7]
    print(Solution().findLHS(nums))