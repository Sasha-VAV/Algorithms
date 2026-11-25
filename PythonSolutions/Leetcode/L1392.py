class Solution:
    def longestPrefix(self, s: str) -> str:
        hash1 = 0
        hash2 = 0
        mult = 1
        mod = 10 ** 9 + 8 # collision not safe add full check
        base = ord('a')
        res = 0
        for i in range(len(s) - 1):
            first = ord(s[i]) - base
            last = ord(s[-i - 1]) - base
            hash1 = (hash1 * 26 + first) % mod
            hash2 = (hash2 + mult * last) % mod
            mult *= 26
            mult %= mod
            if hash1 == hash2:
                res = i + 1
        return s[:res]