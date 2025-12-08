class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        n2 = n**2
        for a in range(1, n):
            a **= 2
            for b in range(1, n):
                b **= 2
                x = (a + b) ** 0.5
                if round(x, 6) == round(x) and a + b <= n2: res += 1
        return res