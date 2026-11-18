class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        prev = "0"
        for i, c in enumerate(s):
            if i & 1 and c != prev:  
                res += 1
            prev = c
        return res