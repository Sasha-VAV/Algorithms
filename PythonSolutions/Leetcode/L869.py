from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        x = 1
        counter = Counter(str(n))
        while x < n // 10:
            x *= 2
        a = str(x)
        n = len(str(n))
        while len(a) <= n:
            if Counter(a) == counter: return True
            x *= 2
            a = str(x)
        return False


if __name__ == '__main__':
    print(Solution().reorderedPowerOf2(56635))