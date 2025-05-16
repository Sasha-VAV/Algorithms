from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [0]
        for i, group in enumerate(groups[1:]):
            if group != groups[res[-1]]:
                res.append(i+1)
        return [words[i] for i in res]