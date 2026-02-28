class Solution:
    def concatenatedBinary(self, n: int) -> int:
        def get_base(value, start=1, base=2):
            for base_power in range(start, 32):
                if value < base:
                    return base_power, base
                base *= 2
            raise ValueError
        res = 0
        curr_base_power = 1
        curr_base = 2
        mod = 10 ** 9 + 7
        for i in range(1, n+1):
            curr_base_power, curr_base = get_base(i, curr_base_power, curr_base)
            res <<= curr_base_power
            res += i
            res %= mod
        return res