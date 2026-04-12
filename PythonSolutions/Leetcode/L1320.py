import string
from collections import Counter


class Solution:
    def minimumDistance(self, word: str) -> int:
        m = len(word)
        ref = string.ascii_uppercase
        n = 6
        arr = [ref.index(c) for c in word]
        dp = [[[None] * m for _ in range(26)] for _ in range(26)]
        for i, c in enumerate(arr):
            y, x = divmod(c, n)
            for left in range(26):
                ly_shift, lx_shift = divmod(left, n)
                for right in range(26):
                    ry_shift, rx_shift = divmod(right, n)
                    if i > 0:
                        prev = dp[left][right][i - 1]
                    else:
                        prev = 0
                    if prev is None: 
                        continue
                    d1 = abs(x - lx_shift) + abs(y - ly_shift)
                    d2 = abs(x - rx_shift) + abs(y - ry_shift)
                    if dp[c][right][i] is None:
                        dp[c][right][i] = prev + d1
                    else:
                        dp[c][right][i] = min(dp[c][right][i], prev + d1)
                    
                    if dp[left][c][i] is None:
                        dp[left][c][i] = prev + d2
                    else:
                        dp[left][c][i] = min(dp[left][c][i], prev + d2)
        res = float('inf')
        for left in range(26):
            for right in range(26):
                if dp[left][right][-1] is not None:
                    res = min(res, dp[left][right][-1])
        return res



if __name__ == "__main__":
    word = "CAKE"
    print(Solution().minimumDistance(word))