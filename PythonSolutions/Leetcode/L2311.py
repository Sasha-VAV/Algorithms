class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s) - 1
        i = n
        x = 0
        res = s.count("0")
        while i >= 0 and x <= k:
            if s[i] == "1":
                x += 2 ** (n - i)
                res += 1
            i -= 1
        if x > k:
            res -= 1
        return res


if __name__ == '__main__':
    s = "1001010"
    k = 5
    print(Solution().longestSubsequence(s, k))