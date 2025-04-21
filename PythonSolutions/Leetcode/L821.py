class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [0] * len(s)
        idx = s.find(c)
        j = s.find(c, idx+1)
        j = 2 * len(s) if j == -1 else j
        for i, x in enumerate(s):
            res[i] = min(abs(j-i), abs(idx - i))
            if abs(j - i) < abs(idx - i) and j > -1:
                idx = j
                j = s.find(c, idx+1)
        return res