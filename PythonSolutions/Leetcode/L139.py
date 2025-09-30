from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = defaultdict(list)
        for word in wordDict:
            a = s.find(word)
            while a != -1:
                words[a].append(word)
                a = s.find(word, a + 1)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == len(s): return True
            if i not in words: return False
            for x in words[i]:
                if dfs(i + len(x)): return True
            return False

        return dfs(0)