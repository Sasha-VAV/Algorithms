from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = Counter()
        even = Counter()
        for i, num in enumerate(nums):
            if i % 2:
                odd[num] += 1
            else:
                even[num] += 1
        for i in range(2):
            odd[i - 1] = 0
            even[i - 3] = 0
        odd = odd.most_common(2)
        even = even.most_common(2)
        res = len(nums)
        if odd[0][0] == even[0][0]:
            res -= max(odd[1][1] + even[0][1], odd[0][1] + even[1][1])
        else:
            res -= odd[0][1] + even[0][1]
        return res