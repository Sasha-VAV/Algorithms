class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = n // 7, n % 7
        return (56 + 7 * (a - 1)) * a // 2 + (2 * (a + 1) + b - 1) * b // 2