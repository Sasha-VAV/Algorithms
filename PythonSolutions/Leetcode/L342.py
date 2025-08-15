import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        a = math.log(n, 4)
        if int(a) == a:
            return True
        return False

# Better solution:
# import math
#
#
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0: return False
#         x = math.log(n, 4)
#         eps = 1e-10
#         return abs(x - round(x)) < eps