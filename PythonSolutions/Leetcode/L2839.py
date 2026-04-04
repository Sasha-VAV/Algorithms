class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a1 = set(c for i, c in enumerate(s1) if i % 2 == 0)
        b1 = set(c for i, c in enumerate(s2) if i % 2 == 0)
        a2 = set(c for i, c in enumerate(s1) if i % 2 == 1)
        b2 = set(c for i, c in enumerate(s2) if i % 2 == 1)
        return a1 == b1 and a2 == b2