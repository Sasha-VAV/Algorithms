from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        counter = Counter(words)
        x = False
        for word, count in counter.items():
            if word[0] == word[1]:
                res += count // 2 * 4
                if not x:
                    x = count % 2 == 1
                    res += 2 * int(x)
            elif word[::-1] in counter:
                a = min(count, counter[word[::-1]])
                res += a * 4
                counter[word[::-1]] -= a
                counter[word] -= a
        return res


if __name__ == '__main__':
    words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    print(Solution().longestPalindrome(words))