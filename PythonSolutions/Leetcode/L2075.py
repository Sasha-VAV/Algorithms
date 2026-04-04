class Solution:
    def decodeCiphertext(self, text: str, rows: int) -> str:
        n = len(text)
        if n % rows != 0: raise ValueError(f"{n=}, {rows=}")
        n //= rows
        res = [""] * n * rows
        for i, c in enumerate(text):
            y, x = divmod(i, n)
            if y > x: continue
            res[(x - y)*rows+y] = c
        return "".join(res).rstrip()


if __name__ == '__main__':
    text = "ch   ie   pr"
    rows = 3
    print(Solution().decodeCiphertext(text, rows))