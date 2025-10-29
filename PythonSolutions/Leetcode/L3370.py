class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2 ** math.ceil(math.log2(n) + 1e-9) - 1