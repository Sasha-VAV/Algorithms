class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        letters = set(brokenLetters)
        for word in text.split():
            if set(word).intersection(letters): continue
            res += 1
        return res