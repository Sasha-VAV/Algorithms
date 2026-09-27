class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def check(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = 0
        n = len(s)
        start = 0
        for r in range(k - 1, n):
            l = r - k + 1
            if l >= start and check(l, r):
                start = r + 1
                res += 1
                continue
            l = r - k
            if l >= start and check(l, r):
                start = r + 1
                res += 1
        return res