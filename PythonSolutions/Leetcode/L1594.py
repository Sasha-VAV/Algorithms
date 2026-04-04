from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[None, None]] * len(grid[0])
        x = grid[0][0]
        if x == 0:
            return 0
        elif x < 0:
            dp[0] = [x, None]
        else:
            dp[0] = [None, x]

        zero_exist = False
        mod = 10**9 + 7
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i == 0 and j == 0:
                    continue
                if x == 0:
                    zero_exist = True
                    dp[j] = None, None
                    continue
                l_min, l_max = None, None
                if j > 0:
                    l_min, l_max = dp[j-1]
                up_min, up_max = dp[j]
                def find_best(a, b, func, value):
                    if a and b:
                        return func(a, b) * value
                    elif a:
                        return a * value
                    elif b:
                        return b * value
                    return None

                curr_max = find_best(up_max, l_max, max, x)
                curr_min = find_best(up_min, l_min, min, x)
                if x < 0:
                    curr_max, curr_min = curr_min, curr_max
                if curr_min and curr_min >= 0: curr_min = None
                if curr_max and curr_max <= 0: curr_max = None

                dp[j] = curr_min, curr_max
        res = dp[-1][1]
        if not res and zero_exist:
            return 0
        if res is None:
            return -1
        return res % mod


if __name__ == "__main__":
    arr = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    print(Solution().maxProductPath(arr))