class Solution:
    def reverseDegree(self, s: str) -> int:
        z = ord('z')
        return sum(i * (z - ord(c) + 1) for i, c in enumerate(s, start=1))