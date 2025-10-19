from typing import List
from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for word1, word2 in zip(words, words[1:]):
            if Counter(word1) != Counter(word2):
                res.append(word2)
        return res