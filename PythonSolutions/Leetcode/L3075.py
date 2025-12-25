from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        decrease = 0
        for h in happiness:
            if h - decrease <= 0 or k == 0: return res
            res += h - decrease
            decrease += 1
            k -= 1
        return res