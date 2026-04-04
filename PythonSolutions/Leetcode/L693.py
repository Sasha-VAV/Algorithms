class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2
        n >>= 1
        while n > 0:
            if n % 2 == prev:
                return False
            prev = n % 2
            n >>= 1
        return True
