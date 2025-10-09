from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        res = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                res[j + 1] = max(res[j], res[j+1]) + mana[i] * skill[j]
            for j in range(n - 1, 0, -1):
                res[j] = res[j + 1] - mana[i] * skill[j]
        return res[-1]