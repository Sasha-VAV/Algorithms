from collections import Counter
from typing import List


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter1 = Counter(nums1)
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.counter2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for k, v in self.counter1.items():
            res += v * self.counter2[tot - k]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)