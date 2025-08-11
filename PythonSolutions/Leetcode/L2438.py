from functools import lru_cache
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = 10 ** 9 + 7
        @lru_cache(maxsize=None)
        def pow2(k):
            if k == 0: return 1
            if k % 2 == 0: return pow2(k//2) ** 2 % mod
            return 2 * pow2(k - 1) % mod
        for i, x in enumerate(bin(n)[2:][::-1]):
            if x == "0": continue
            powers.append(pow2(i))
        products = [1] * (len(powers) + 1)
        for i, x in enumerate(powers):
            products[i+1] = products[i] * x
        res = []
        for l, r in queries:
            res.append((products[r+1] // products[l]) % mod)
        return res