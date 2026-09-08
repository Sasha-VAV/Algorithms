import math


class Solution:
    def countCommas(self, n: int) -> int:
        length = int(math.log(n, 10) + 1e-12) + 1
        res = 0
        curr = 9
        for i in range(length - 1):
            res += (i // 3) * curr
            curr *= 10
        res += ((length - 1) // 3) * (n - curr // 9 + 1)
        return res


if __name__ == "__main__":
    print(Solution().countCommas(10020))
