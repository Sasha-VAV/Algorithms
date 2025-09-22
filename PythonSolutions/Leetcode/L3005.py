from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_val = max(counter.values())
        return sum(x for x in counter.values() if x == max_val)
