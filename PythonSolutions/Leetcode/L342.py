import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        a = math.log(n, 4)
        if int(a) == a:
            return True
        return False