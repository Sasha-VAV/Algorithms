class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        char_set = set()
        for c1, c2 in zip(s, t):
            if c1 in mapping and c2 != mapping[c1] or c1 not in mapping and c2 in char_set:
                return False
            mapping[c1] = c2
            char_set.add(c2)
        return True