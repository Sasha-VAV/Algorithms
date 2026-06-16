class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalpha():
                res.append(c)
            elif c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res = res * 2
            elif c == "%":
                res.reverse()
            else:
                raise NotImplementedError()
        return "".join(res)