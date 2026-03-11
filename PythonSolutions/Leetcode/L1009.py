class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        power = math.log2(n)
        power = int(power + 1)
        return abs(2 ** power   - n - 1)