class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        had_zero = False
        for c in s:
            if c == "0":
                had_zero = True
            if c == "1" and had_zero:
                return False
        return True