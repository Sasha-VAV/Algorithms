from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        odd = []
        even = []
        for k, v in counter.items():
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        return max(odd) - min(even)