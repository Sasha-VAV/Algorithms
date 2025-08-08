import math
from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000: return 1
        @lru_cache(maxsize=None)
        def f(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            return 0.25 * (f(a-1, b-3) + f(a-2,b-2) + f(a-3,b-1) + f(a-4,b))
        n = math.ceil(n / 25.0)
        return f(n,n)