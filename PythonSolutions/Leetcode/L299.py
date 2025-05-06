class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = Counter(secret)
        b = Counter(guess)
        res = 0
        for k, v in a.items():
            if k in b:
                res += min(v, b[k])
        x = 0
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                x += 1
        return f"{x}A{res-x}B"