class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        prev = 0
        mod = 10 ** 9 + 7
        for c in s:
            if c == "1":
                prev += 1
                res += prev
                res %= mod
            else:
                prev = 0
        return res