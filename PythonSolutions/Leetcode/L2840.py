class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        c11 = Counter(s1[::2])
        c12 = Counter(s1[1::2])
        c21 = Counter(s2[::2])
        c22 = Counter(s2[1::2])
        return c11 == c21 and c12 == c22