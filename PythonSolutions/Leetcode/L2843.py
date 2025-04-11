class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        k = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                k += 1
            elif a > 999 and a // 1000 + a // 100 % 10 == a % 100 // 10 + a % 10:
                k += 1
        return k
