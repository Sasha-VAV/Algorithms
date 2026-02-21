class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        @cache
        def is_prime(value):
            if value < 2: return False
            for v in range(2, int(math.sqrt(value) + 1)):
                if is_prime(v):
                    if not value % v: return False
            return True

        for x in range(left, right+1):
            x = x.bit_count()
            if is_prime(x): res += 1
        return res