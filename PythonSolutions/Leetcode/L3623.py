from typing import List
import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        res = 0
        prev = None
        bank = 0
        curr = 0
        points = sorted(points, key=lambda k: (k[1], k[0]))
        points.append([0, points[-1][1] + 1])
        for x, y in points:
            if y != prev:
                if curr > 0:
                    curr_combinations = math.comb(curr, 2) % mod
                else:
                    curr_combinations = 0
                res += bank * curr_combinations
                res %= mod
                bank += curr_combinations
                curr = 0
            prev = y
            curr += 1
        return round(res)


if __name__ == '__main__':
    arr = [[1,0],[2,0],[3,0],[2,2],[3,2]]
    print(Solution().countTrapezoids(arr))