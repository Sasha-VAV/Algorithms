class Solution:
    def maxProduct(self, n: int) -> int:
        a, b = list(sorted(map(int, str(n))))[-2:]
        return a * b