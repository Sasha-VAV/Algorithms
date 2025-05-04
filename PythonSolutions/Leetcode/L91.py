class Solution:
    def numDecodings(self, s: str) -> int:
        i = 0
        n = len(s)
        cache = dict()
        def decode(i):
            if s[i] == '0':
                return 0
            if i == n - 1:
                return 1
            if i in cache:
                return cache[i]
            res = decode(i+1)
            if s[i] == '1' or s[i] == '2' and s[i+1] in '0123456':
                res += decode(i+2) if i < n - 2 else 1
            cache[i] = res
            return res
        return decode(0)