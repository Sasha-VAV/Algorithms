class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        prev_a = b > a
        while a or b:
            if prev_a:
                if b == 0:
                    raise ValueError
                if b > a and b > 1:
                    res.append("bb")
                    b -= 2
                else:
                    res.append("b")
                    b -= 1
                prev_a = False
            else:
                if a == 0:
                    raise ValueError
                if a > b and a > 1:
                    res.append("aa")
                    a -= 2
                else:
                    res.append("a")
                    a -= 1
                prev_a = True
        return "".join(res)