class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        n = len(s) - 1
        for i, c in enumerate(reversed(s)):
            x = int(c) + carry
            if i == n:
                break
            if x % 2 == 1:
                x += 1
                res += 1
            res += 1
            carry = x // 2
        match x:
            case 1:
                return res
            case 2:
                return res + 1
            case 3:
                return res + 3