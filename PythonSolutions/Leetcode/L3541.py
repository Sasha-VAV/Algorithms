class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowels = 0
        consonants = 0
        for k, v in counter.items():
            if k in "aeiou":
                vowels = max(v, vowels)
            else:
                consonants = max(v, consonants)
        return vowels + consonants