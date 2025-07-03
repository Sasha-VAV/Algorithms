import math


class Solution:
    def kthCharacter(self, k: int) -> str:
        n = 2 ** math.ceil(math.log(k, 2))
        res = 0
        while k > 1:
            n //= 2
            if k > n:
                k -= n
                res += 1
        return chr(ord('a') + res)


if __name__ == '__main__':
    print(Solution().kthCharacter(5))