class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        res = 0
        for k, v1 in c1.items():
            v2 = c2[k]
            if v1 > v2:
                res += v1 - v2
        return res
            