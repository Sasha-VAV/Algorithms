class Solution:
    def kMirror(self, k: int, n: int) -> int:
        res = 0
        def convert(number, base):
            arr = []
            while number > 0:
                arr.append(number % base)
                number //= base
            return 0 if arr[::-1] != arr else 1

        i = 0
        for j in "123456789":
            x = int(j)
            if convert(x, k) != 0:
                n -= 1
                res += x
                if n == 0: return res
        while True:
            for x in range(10 ** i, 10 ** (i + 1)):
                x = int(str(x) + str(x)[::-1])
                if convert(x, k) != 0:
                    n -= 1
                    res += x
                    if n == 0: return res
            for x in range(10 ** i, 10 ** (i + 1)):
                for j in "0123456789":
                    a = int(str(x) + j + str(x)[::-1])
                    if convert(a, k) != 0:
                        n -= 1
                        res += a
                        if n == 0: return res
            i += 1


if __name__ == '__main__':
    print(Solution().kMirror(5, 20))