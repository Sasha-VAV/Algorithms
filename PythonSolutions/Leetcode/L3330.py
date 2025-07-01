class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 0
        x = word[0]
        for c in word:
            if c != x:
                x = c
            else:
                res += 1
        return res