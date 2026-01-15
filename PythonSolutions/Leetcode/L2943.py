from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def max_increasing(arr: list):
            arr.sort()
            prev = arr[0] - 2
            res = -1
            curr = 1
            for x in arr:
                if x - prev != 1:
                    res = max(res, curr)
                    curr = 0
                curr += 1
                prev = x
            return max(res, curr) + 1
        return min(max_increasing(hBars), max_increasing(vBars)) ** 2