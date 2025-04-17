class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first = bool(s) and (s[0] == p[0] or p[0] == ".")
        if len(p) > 1 and p[1] == "*":
            return first and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            return first and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    print(Solution().isMatch("aaa", "aaaa"))