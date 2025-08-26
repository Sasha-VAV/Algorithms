from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = 0
        x = 0
        for a, b in dimensions:
            y = a ** 2 + b ** 2
            if y > x:
                x = y
                res = a * b
            elif y == x:
                res = max(res, a * b)
        return res