import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = re.sub(r'(\*)+', r'\1', p)
        ls = len(s)
        lp = len(p)
        cache = dict()
        def match(s_i, p_i):
            if (s_i, p_i) in cache:
                return cache[(s_i, p_i)]
            if p_i < lp and p[p_i] == "*" and s_i == ls:
                cache[(s_i, p_i)] = match(s_i, p_i+1)
                return cache[(s_i, p_i)]
            if s_i == ls or p_i == lp:
                if s_i == ls and p_i == lp:
                    cache[(s_i, p_i)] = True
                    return True
                cache[(s_i, p_i)] = False
                return False
            if p[p_i] == "?" or p[p_i] == s[s_i]:
                cache[(s_i, p_i)] = match(s_i+1, p_i+1)
                return cache[(s_i, p_i)]
            if p[p_i] == "*":
                cache[(s_i, p_i)] =  match(s_i+1, p_i) or match(s_i, p_i+1) or match(s_i+1, p_i+1)
                return cache[(s_i, p_i)]
            cache[(s_i, p_i)] = False
            return False
        return match(0,0)