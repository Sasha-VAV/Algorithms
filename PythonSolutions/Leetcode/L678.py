class Solution:
    def checkValidString(self, s: str) -> bool:
        l = 0
        h = 0
        for c in s:
            if c == "(":
                l += 1
                h += 1
            elif c == ")":
                h -= 1
                l -= 1
            else:
                l -= 1
                h += 1
            if h < 0:
                return False
            l = max(l, 0)

        return l == 0