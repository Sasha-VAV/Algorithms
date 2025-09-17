from typing import List
from math import gcd, lcm


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            res.append(x)
            while len(res) > 1 and gcd(res[-1], res[-2]) > 1:
                res.append(lcm(res.pop(), res.pop()))
        return res