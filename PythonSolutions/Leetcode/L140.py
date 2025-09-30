from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = defaultdict(list)
        for word in wordDict:
            a = s.find(word)
            while a != -1:
                words[a].append(word)
                a = s.find(word, a + 1)
        answers = set()
        def dfs(i, arr):
            if i == len(s):
                answers.add(" ".join(arr))
                return
            if i not in words: return
            for x in words[i]:
                dfs(i + len(x), arr + [x])
            return
        dfs(0, [])
        return list(answers)