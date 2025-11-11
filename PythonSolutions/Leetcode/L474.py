from functools import lru_cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [[s.count("0"), s.count("1")] for s in strs]
        @lru_cache(maxsize=None)
        def dp(x, y, i):
            if x < 0 or y < 0: return -1
            if i == len(strs): return 0
            return max(dp(x, y, i + 1), 1 + dp(x - counts[i][0], y - counts[i][1], i + 1))
        return dp(m, n, 0)