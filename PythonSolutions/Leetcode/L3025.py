from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        for a, b in points:
            for c, d in points:
                if (a, b) == (c, d): continue
                if a > c or b < d: continue
                for x, y in points:
                    if (x, y) == (a, b) or (x, y) == (c, d): continue
                    if a <= x <= c and d <= y <= b: break
                else:
                    res += 1
        return res