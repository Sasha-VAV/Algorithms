class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        vowels = {'a', 'e', 'i', 'o', 'u'}
        consonants = set("bcdfghjklmnpqrstvwxyz")
        nums = set("0123456789")
        word = set(word.lower())
        if len(word.intersection(vowels)) > 0 and len(word.intersection(consonants)) > 0 and len(word.intersection(nums.union(vowels.union(consonants)))) == len(word): return True
        return False
