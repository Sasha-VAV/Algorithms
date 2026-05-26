class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters = set(word)
        res = 0
        for c in letters:
            if c.islower() and c.upper() in letters:
                res += 1
        return res