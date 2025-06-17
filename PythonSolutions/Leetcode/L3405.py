import math


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        if k == 0:
            c = 1
        else:
            c = math.comb(n - 1, k) % mod
        res = m * c
        def pow(x, p):
            if p == 0:
                return 1
            if p % 2 == 0:
                return pow(x, p // 2) ** 2 % mod
            return x * pow(x, p - 1) % mod
        return res * pow(m - 1, n - 1 - k) % mod


if __name__ == '__main__':
    print(Solution().countGoodArrays(5581, 58624, 4766))