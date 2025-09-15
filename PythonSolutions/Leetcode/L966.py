from typing import List
import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res = []
        set_wordlist = set(wordlist)
        lowers = {word.lower(): word for word in wordlist[::-1]}
        def mask(string) -> str:
            return "".join(["_" if c in "aeiou" else c for c in string.lower()])
        corrections = {mask(word): word for word in wordlist[::-1]}
        for query in queries:
            if query in set_wordlist:
                res.append(query)
                continue
            if query.lower() in lowers:
                res.append(lowers[query.lower()])
                continue
            if mask(query) in corrections:
                res.append(corrections[mask(query)])
                continue
            res.append("")
        return res


if __name__ == '__main__':
    wordlist = ["KiTe", "kite", "hare", "Hare"]
    queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
    print(Solution().spellchecker(wordlist, queries))