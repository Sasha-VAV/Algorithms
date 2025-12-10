from collections import Counter
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        counter = Counter(complexity)
        min_val = min(complexity)
        if min_val != complexity[0] or counter[min_val] > 1: return 0
        mod = 10**9 + 7
        def factorial(n):
            if n == 1: return 1
            return n * factorial(n - 1) % mod
        return factorial(len(complexity) - 1) % mod