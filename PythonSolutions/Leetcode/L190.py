from functools import lru_cache


class Solution:
    @lru_cache(None)
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            res += n % 2
            n = n >> 1
        return res