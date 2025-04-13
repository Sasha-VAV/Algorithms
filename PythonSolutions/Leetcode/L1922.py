class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def quick_power(x, p):
            if p == 0:
                return 1
            if p == 1:
                return x
            if p % 2 == 0:
                return quick_power(x, p // 2) ** 2 % mod
            return quick_power(x, p - 1) * x % mod
        return quick_power(20, n//2) * 5 ** (n%2) % mod