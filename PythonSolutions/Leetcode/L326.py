import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        x = math.log(n, 3)
        eps = 1e-10
        return abs(round(x) - x) < eps


if __name__ == '__main__':
    print(Solution().isPowerOfThree(14348906))