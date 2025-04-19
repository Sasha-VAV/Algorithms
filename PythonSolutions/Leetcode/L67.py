class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        n = len(a)
        m = len(b)
        a = list(a)
        b = list(b)
        c = "0"
        for i in range(1, n+1):
            x = a[-i]
            y = b[-i] if i <= m else "0"
            x = (x + y + c).count("1")
            a[-i] = str(x % 2)
            c = str(x // 2)
        if c == "1":
            a.insert(0, "1")
        return "".join(a)


if __name__ == "__main__":
    print(Solution().addBinary("101111", "10"))